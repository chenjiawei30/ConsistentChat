#!/usr/bin/env python3
"""
Test Script for Multi-turn Dialogue Generation

This script tests the dialogue generator with clean data structure and validates
all functionality including data loading, template processing, and dialogue generation.

Author: Your Name
License: MIT
Version: 1.0.0
"""

import json
import os
from dialogue_generator import DialogueGenerator
from config import API_CONFIG, FILE_PATHS, GENERATION_CONFIG


def test_config_loading():
    """Test configuration loading"""
    print("=== Testing Configuration Loading ===")
    
    try:
        print(f"API Configuration: {API_CONFIG}")
        print(f"File Path Configuration: {FILE_PATHS}")
        print(f"Generation Configuration: {GENERATION_CONFIG}")
        print("✓ Configuration loading successful")
        return True
    except Exception as e:
        print(f"❌ Configuration loading failed: {e}")
        return False


def test_data_structure():
    """Test simplified data structure"""
    print("\n=== Testing Simplified Data Structure ===")
    
    try:
        data_path = FILE_PATHS["data"]
        if not os.path.exists(data_path):
            print("❌ Simplified data file does not exist")
            return False
        
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check structure
        if "categories" not in data:
            print("❌ Missing 'categories' in data structure")
            return False
        
        if "flow_definitions" not in data:
            print("❌ Missing 'flow_definitions' in data structure")
            return False
        
        categories = data["categories"]
        flow_definitions = data["flow_definitions"]
        
        print(f"✓ Found {len(categories)} categories")
        print(f"✓ Found {len(flow_definitions)} flow definitions")
        
        # Check each category has required fields
        for category_name, category_data in categories.items():
            if "scenarios" not in category_data:
                print(f"❌ Category '{category_name}' missing 'scenarios'")
                return False
            if "flow_type" not in category_data:
                print(f"❌ Category '{category_name}' missing 'flow_type'")
                return False
            
            flow_type = category_data["flow_type"]
            if flow_type not in flow_definitions:
                print(f"❌ Category '{category_name}' references unknown flow_type '{flow_type}'")
                return False
        
        print("✓ All categories have valid structure")
        return True
        
    except Exception as e:
        print(f"❌ Data structure test failed: {e}")
        return False


def test_dialogue_generator():
    """Test simplified dialogue generator"""
    print("\n=== Testing Simplified Dialogue Generator ===")
    
    try:
        # Initialize generator
        generator = DialogueGenerator(
            base_url=API_CONFIG["base_url"],
            api_key=API_CONFIG["api_key"],
            model=API_CONFIG["model"]
        )
        print("✓ Successfully initialized dialogue generator")
        
        # Test loading data
        data = generator.load_data(FILE_PATHS["data"])
        categories = data.get("categories", {})
        flow_definitions = data.get("flow_definitions", {})
        print(f"✓ Successfully loaded data, total {len(categories)} categories")
        
        # Test loading templates
        query_template = generator.load_prompt_template(FILE_PATHS["query_prompt"])
        response_template = generator.load_prompt_template(FILE_PATHS["response_prompt"])
        print("✓ Successfully loaded prompt templates")
        
        # Test single dialogue generation
        print("\nStarting single dialogue generation test...")
        test_category = "Problem-solving Interaction"
        test_scenario = "Technical Support"
        test_flow_type = "problem_diagnosis_to_solution"
        
        dialogue = generator.generate_dialogue(
            category=test_category,
            scenario=test_scenario,
            flow_type=test_flow_type,
            query_prompt_template=query_template,
            response_prompt_template=response_template,
            flow_definitions=flow_definitions
        )
        
        print("✓ Successfully generated test dialogue")
        print(f"Dialogue category: {dialogue['category']}")
        print(f"Dialogue turns: {len(dialogue['turns'])}")
        print(f"Query count: {len(dialogue['queries'])}")
        print(f"Response count: {len(dialogue['responses'])}")
        
        # Save test results
        test_output = "test_simple_output.json"
        with open(test_output, "w", encoding="utf-8") as f:
            json.dump(dialogue, f, ensure_ascii=False, indent=2)
        print(f"✓ Test results saved to {test_output}")
        
        return True
        
    except Exception as e:
        print(f"❌ Dialogue generator test failed: {e}")
        return False


def main():
    """Main test function"""
    print("Starting tests for simplified dialogue generation...")
    
    tests = [
        test_config_loading,
        test_data_structure,
        test_dialogue_generator
    ]
    
    passed = 0
    total = len(tests)
    
    for test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"Test {test_func.__name__} encountered exception: {e}")
    
    print(f"\n=== Test Results ===")
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed! Simplified version is working properly.")
    else:
        print("⚠ Some tests failed. Please check the configuration and data structure.")


if __name__ == "__main__":
    main()
