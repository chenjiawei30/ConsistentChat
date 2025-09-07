# API Configuration
# Update these settings according to your LLM API provider
# API_CONFIG = {
#     "base_url": "https://api.openai.com/v1",  # OpenAI API endpoint
#     "api_key": "sk-your-openai-api-key-here",  # Your OpenAI API key
#     "model": "gpt-4o",  # Model name to use
# }

# Alternative configurations for other providers:

# For Anthropic Claude:
# API_CONFIG = {
#     "base_url": "https://api.anthropic.com/v1",
#     "api_key": "sk-ant-your-claude-api-key-here",
#     "model": "claude-3-sonnet-20240229",
# }

# For local LLM server (e.g., vLLM, SGLang):
API_CONFIG = {
    "base_url": "http://localhost:7813/v1",  # Your local endpoint
    "api_key": "sk-xxx",  # Usually not needed for local servers, put non-empty string
    "model": "Qwen-2.5-72B-Instruct",  # Your local model name
}

# File path configuration
FILE_PATHS = {
    "data": "data/dummy_data.json",  # Main data file with categories and flow definitions
    "query_prompt": "prompt/query_template_en.txt",  # Query generation template
    "response_prompt": "prompt/response_template_en.txt",  # Response generation template
    "output_file": "generated_dialogues.json",  # Output file for batch generation
    "test_output": "test_dialogue.json"  # Output file for test generation
}

# Generation configuration
GENERATION_CONFIG = {
    "max_tokens_query": 800,  # Maximum tokens when generating queries
    "max_tokens_response": 1200,  # Maximum tokens when generating responses
    "temperature_query": 0.8,  # Temperature for query generation (0.0-2.0)
    "temperature_response": 0.7,  # Temperature for response generation (0.0-2.0)
    "max_retries": 3,  # Maximum number of retry attempts for API calls
    "retry_delay": 1  # Delay between retries in seconds
}

# Output configuration
OUTPUT_CONFIG = {
    "ensure_ascii": False,  # Whether to ensure ASCII encoding in JSON output
    "indent": 2  # JSON indentation level
}
