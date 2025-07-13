#!/usr/bin/env python3
"""
Basic usage examples for the AI Assistant with Ollama

This script demonstrates common use cases and patterns.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_assistant import AIAssistant, ChatMessage

def example_basic_chat():
    """Example: Basic chat interaction"""
    print("🔵 Basic Chat Example")
    print("-" * 30)
    
    assistant = AIAssistant(model="llama3.2:3b")
    
    if not assistant.setup():
        print("Failed to setup assistant")
        return
    
    # Single question
    response = assistant.chat("What is machine learning?")
    print(f"Response: {response[:100]}...")
    
    # Follow-up question (uses history)
    response = assistant.chat("Can you give me a simple example?")
    print(f"Follow-up: {response[:100]}...")

def example_story_generation():
    """Example: Creative story generation"""
    print("\n🟢 Story Generation Example")
    print("-" * 30)
    
    assistant = AIAssistant()
    
    if not assistant.setup():
        return
    
    prompts = [
        "a detective solving a mystery in space",
        "a dragon who is afraid of flying",
        "a programmer who discovers their code is alive"
    ]
    
    for prompt in prompts:
        print(f"\nPrompt: {prompt}")
        print("Story:")
        story = assistant.generate_story(prompt)
        print(f"Generated story: {story[:200]}...")

def example_code_review():
    """Example: Code review functionality"""
    print("\n🟡 Code Review Example")
    print("-" * 30)
    
    assistant = AIAssistant()
    
    if not assistant.setup():
        return
    
    code_samples = [
        """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
""",
        """
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
""",
        """
class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        return a / b
"""
    ]
    
    for i, code in enumerate(code_samples, 1):
        print(f"\nCode Sample {i}:")
        print(code.strip())
        print("\nReview:")
        review = assistant.code_review(code)
        print(f"Review: {review[:300]}...")

def example_context_management():
    """Example: Managing conversation context"""
    print("\n🟣 Context Management Example")
    print("-" * 30)
    
    assistant = AIAssistant()
    
    if not assistant.setup():
        return
    
    # Build context over multiple exchanges
    topics = [
        "Let's talk about Python programming",
        "What are some best practices for writing clean code?",
        "How do these apply to the language we were discussing?",
        "Can you give me an example using that language?"
    ]
    
    for topic in topics:
        print(f"\nUser: {topic}")
        print("Assistant: ", end="")
        response = assistant.chat(topic)
        print(f"{response[:150]}...")
    
    # Clear context and start fresh
    assistant.clear_history()
    print("\n[Context cleared]")
    
    # This should not reference previous conversation
    print("\nUser: What language were we discussing?")
    print("Assistant: ", end="")
    response = assistant.chat("What language were we discussing?")
    print(f"{response[:150]}...")

def example_different_models():
    """Example: Using different models"""
    print("\n🔴 Different Models Example")
    print("-" * 30)
    
    models = ["llama3.2:3b", "llama3.2:1b", "codellama:7b"]
    question = "Write a simple Python function to calculate fibonacci numbers"
    
    for model in models:
        print(f"\nTesting model: {model}")
        assistant = AIAssistant(model=model)
        
        if assistant.setup():
            response = assistant.chat(question, use_history=False)
            print(f"Response: {response[:200]}...")
        else:
            print(f"Model {model} not available")

def interactive_example():
    """Interactive example - mini chat session"""
    print("\n🔶 Interactive Example")
    print("-" * 30)
    print("Type 'quit' to exit this example")
    
    assistant = AIAssistant()
    
    if not assistant.setup():
        return
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'quit':
            break
        elif user_input:
            print("AI: ", end="")
            assistant.chat(user_input)

if __name__ == "__main__":
    print("🤖 AI Assistant Examples")
    print("=" * 40)
    
    try:
        example_basic_chat()
        example_story_generation()
        example_code_review()
        example_context_management()
        example_different_models()
        
        # Optional interactive session
        response = input("\nWould you like to try interactive mode? (y/n): ")
        if response.lower().startswith('y'):
            interactive_example()
            
    except KeyboardInterrupt:
        print("\n\nExiting...")
    except Exception as e:
        print(f"Error: {e}")
        
    print("\n✅ Examples completed!")
