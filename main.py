import json
import sys
from dialogue_generator import DialogueGenerator
from config import API_CONFIG, FILE_PATHS, GENERATION_CONFIG


def main():
    print("=== Skeleton-Guided Multi-turn Dialogue Generation ===")
    
    try:
        # Initialize generator
        generator = DialogueGenerator(
            base_url=API_CONFIG["base_url"],
            api_key=API_CONFIG["api_key"],
            model=API_CONFIG["model"]
        )
        
        # Load data
        print("Loading data...")
        data = generator.load_data(FILE_PATHS["data"])
        categories = data.get("categories", {})
        print(f"✓ Successfully loaded {len(categories)} categories")
        
        # Load prompt templates
        print("Loading prompt templates...")
        query_prompt_template = generator.load_prompt_template(FILE_PATHS["query_prompt"])
        response_prompt_template = generator.load_prompt_template(FILE_PATHS["response_prompt"])
        print("✓ Successfully loaded prompt templates")
        
        # Start batch generation
        print("\nStarting batch dialogue generation...")
        all_dialogues = generator.batch_generate(
            data=data,
            query_prompt_template=query_prompt_template,
            response_prompt_template=response_prompt_template,
            output_file=FILE_PATHS["output_file"]
        )
        
        print(f"\n🎉 Generation completed!")
        print(f"Total generated: {len(all_dialogues)} dialogues")
        print(f"Output file: {FILE_PATHS['output_file']}")
        
    except Exception as e:
        print(f"Error during generation: {e}")
        sys.exit(1)


def test_single():
    """Test function for single dialogue generation"""
    print("=== Test Single Dialogue Generation (Simplified) ===")
    
    try:
        # Initialize generator
        generator = DialogueGenerator(
            base_url=API_CONFIG["base_url"],
            api_key=API_CONFIG["api_key"],
            model=API_CONFIG["model"]
        )
        
        # Load data
        data = generator.load_data(FILE_PATHS["data"])
        categories = data.get("categories", {})
        flow_definitions = data.get("flow_definitions", {})
        
        # Load prompt templates
        query_prompt_template = generator.load_prompt_template(FILE_PATHS["query_prompt"])
        response_prompt_template = generator.load_prompt_template(FILE_PATHS["response_prompt"])
        
        # Test generating a dialogue
        test_category = "Problem-solving Interaction"
        test_scenario = "Technical Support"
        test_flow_type = "problem_diagnosis_to_solution"
        
        dialogue = generator.generate_dialogue(
            category=test_category,
            scenario=test_scenario,
            flow_type=test_flow_type,
            query_prompt_template=query_prompt_template,
            response_prompt_template=response_prompt_template,
            flow_definitions=flow_definitions
        )
        
        print("\nGenerated dialogue:")
        print(json.dumps(dialogue, ensure_ascii=False, indent=2))
        
        # Save test results
        with open(FILE_PATHS["test_output"], "w", encoding="utf-8") as f:
            json.dump(dialogue, f, ensure_ascii=False, indent=2)
        print(f"\nTest dialogue saved to {FILE_PATHS['test_output']}")
        
    except Exception as e:
        print(f"Error during test: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_single()
    else:
        main()
