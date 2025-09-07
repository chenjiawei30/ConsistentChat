import json
import os
from typing import List, Dict, Optional
from openai import OpenAI
from jinja2 import Template
from tqdm import tqdm

from config import API_CONFIG, GENERATION_CONFIG, OUTPUT_CONFIG


class DialogueGenerator:
    """
    Multi-turn dialogue generator with clean data structure.
    
    This class provides methods for generating multi-turn dialogues using LLM APIs
    with a simplified data structure and original prompt template compatibility.
    """
    
    def __init__(self, base_url: str, api_key: str, model: str):
        """Initialize the generator with API configuration"""
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = model
        self.max_retries = GENERATION_CONFIG["max_retries"]
        self.retry_delay = GENERATION_CONFIG["retry_delay"]
    
    def load_data(self, data_path: str) -> Dict:
        """Load simplified data file"""
        with open(data_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def load_prompt_template(self, template_path: str) -> str:
        """Load prompt template"""
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def format_flow_steps(self, flow_type: str, flow_definitions: Dict) -> str:
        """Format flow steps for prompt"""
        if flow_type not in flow_definitions:
            return ""
        
        steps = flow_definitions[flow_type]["steps"]
        return f"{flow_type}: {' --> '.join(steps)}"
    
    def call_api_with_retry(self, messages: List[Dict], max_tokens: int = 1024, temperature: float = 0.7) -> str:
        """Call API with retry mechanism"""
        for attempt in range(self.max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    max_tokens=max_tokens,
                    temperature=temperature
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                print(f"API call attempt {attempt + 1} failed: {e}")
                if attempt < self.max_retries - 1:
                    import time
                    time.sleep(self.retry_delay)
                else:
                    raise e
    
    def extract_json_from_response(self, response: str) -> Dict:
        """Extract JSON from API response"""
        # Remove code block markers if present
        if response.startswith("```json") and response.endswith("```"):
            response = response[len("```json"):-len("```")].strip()
        elif response.startswith("```") and response.endswith("```"):
            response = response[len("```"):-len("```")].strip()
        
        return json.loads(response)
    
    def generate_queries(self, category: str, scenario: str, query_prompt_template: str, 
                        flow_steps: str = "") -> List[str]:
        """Generate query questions using original prompt format"""
        context = f"{category} - {scenario}"
        
        # Generate prompt using Jinja2 template
        template = Template(query_prompt_template)
        prompt = template.render(
            context=context,
            info_flows_steps=flow_steps
        )
        
        messages = [{"role": "user", "content": prompt}]
        
        print(f"Generating query questions: {context}")
        response = self.call_api_with_retry(
            messages, 
            max_tokens=GENERATION_CONFIG["max_tokens_query"], 
            temperature=GENERATION_CONFIG["temperature_query"]
        )
        
        try:
            result = self.extract_json_from_response(response)
            queries = result.get("turns", [])
            return queries
            
        except Exception as e:
            print(f"Failed to generate queries: {e}")
            # Return default queries
            return [f"Question {i+1} about {scenario}" for i in range(4)]
    
    def generate_responses(self, category: str, scenario: str, queries: List[str], 
                          response_prompt_template: str) -> List[str]:
        """Generate responses using original prompt format"""
        context = f"{category} - {scenario}\n\nQuestions:\n" + "\n".join([f"Question {i+1}: {q}" for i, q in enumerate(queries)])
        
        # Generate prompt using Jinja2 template
        template = Template(response_prompt_template)
        prompt = template.render(context=context)
        
        messages = [{"role": "user", "content": prompt}]
        
        print(f"Generating responses: {category} - {scenario}")
        response = self.call_api_with_retry(
            messages, 
            max_tokens=GENERATION_CONFIG["max_tokens_response"], 
            temperature=GENERATION_CONFIG["temperature_response"]
        )
        
        try:
            result = self.extract_json_from_response(response)
            responses = result.get("turns", [])
            return responses
            
        except Exception as e:
            print(f"Failed to generate responses: {e}")
            # Return default responses
            return [f"Response {i+1} about {scenario}" for i in range(len(queries))]
    
    def generate_dialogue(self, category: str, scenario: str, flow_type: str, 
                         query_prompt_template: str, response_prompt_template: str, 
                         flow_definitions: Dict) -> Dict:
        """Generate complete multi-turn dialogue"""
        print(f"\nStarting dialogue generation: {category} - {scenario}")
        
        # Format flow steps
        flow_steps = self.format_flow_steps(flow_type, flow_definitions)
        if flow_steps:
            print(f"✓ Using flow type: {flow_type}")
        
        # Step 1: Generate query questions
        queries = self.generate_queries(category, scenario, query_prompt_template, flow_steps)
        print(f"✓ Query generation completed: {len(queries)} questions")
        
        # Step 2: Generate responses
        responses = self.generate_responses(category, scenario, queries, response_prompt_template)
        print(f"✓ Response generation completed: {len(responses)} responses")
        
        # Step 3: Construct dialogue turns
        turns = []
        for i in range(min(len(queries), len(responses))):
            turns.append({
                "human": queries[i],
                "assistant": responses[i]
            })
        
        dialogue_data = {
            "category": f"{category} - {scenario}",
            "turns": turns,
            "queries": queries,
            "responses": responses
        }
        
        print(f"✓ Dialogue generation completed: {len(turns)} turns")
        return dialogue_data
    
    def batch_generate(self, data: Dict, query_prompt_template: str, response_prompt_template: str, 
                       output_file: str):
        """Batch generate dialogue data using simplified structure"""
        all_dialogues = []
        
        categories = data.get("categories", {})
        flow_definitions = data.get("flow_definitions", {})
        
        for category_name, category_data in categories.items():
            print(f"\nProcessing category: {category_name}")
            
            scenarios = category_data.get("scenarios", [])
            flow_type = category_data.get("flow_type", "")
            
            for i, scenario in enumerate(tqdm(scenarios, desc=f"Processing {category_name}")):
                try:
                    dialogue = self.generate_dialogue(
                        category=category_name,
                        scenario=scenario,
                        flow_type=flow_type,
                        query_prompt_template=query_prompt_template,
                        response_prompt_template=response_prompt_template,
                        flow_definitions=flow_definitions
                    )
                    all_dialogues.append(dialogue)
                    
                    # Save to file in real-time
                    with open(output_file, 'w', encoding='utf-8') as f:
                        json.dump(
                            all_dialogues, 
                            f, 
                            ensure_ascii=OUTPUT_CONFIG["ensure_ascii"], 
                            indent=OUTPUT_CONFIG["indent"]
                        )
                    
                    print(f"✓ Saved {len(all_dialogues)} dialogues")
                    
                except Exception as e:
                    print(f"Failed to generate dialogue {category_name} - {scenario}: {e}")
                    continue
        
        print(f"\nBatch generation completed, total generated: {len(all_dialogues)} dialogues")
        return all_dialogues
