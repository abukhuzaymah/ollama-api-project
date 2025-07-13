AI Chat Assistant with Ollama

A Python project demonstrating integration with the Ollama API for local AI model interactions. This project showcases various AI capabilities including chat, story generation, and code review.

## Features

- **Chat Interface**: Interactive conversation with AI models
- **Story Generation**: Creative writing capabilities
- **Code Review**: Automated code analysis and suggestions
- **Streaming Responses**: Real-time response streaming
- **Multiple Models**: Support for different Ollama models
- **Chat History**: Maintains conversation context

## Prerequisites

1. **Install Ollama**: Download and install Ollama from [ollama.ai](https://ollama.ai/)
2. **Start Ollama Server**: Run `ollama serve` in your terminal
3. **Pull a Model**: Download a model like `ollama pull llama3.2:3b`

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd ollama-ai-assistant

Install dependencies:

bashpip install -r requirements.txt

Ensure Ollama is running:

bashollama serve
Usage
Basic Usage
bashpython ai_assistant.py
This will run the demo script showing various capabilities.
Programmatic Usage
pythonfrom ai_assistant import AIAssistant

# Initialize the assistant
assistant = AIAssistant(model="llama3.2:3b")

# Setup (checks connection and model availability)
if assistant.setup():
    # Chat with the assistant
    response = assistant.chat("Hello! How are you?")
    
    # Generate a story
    story = assistant.generate_story("a time-traveling scientist")
    
    # Review code
    code_review = assistant.code_review("def hello(): print('world')")
Project Structure
├── ai_assistant.py      # Main application code
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── examples/           # Example usage scripts
API Classes
OllamaClient

Low-level client for Ollama API interactions
Handles model management, chat, and generation requests
Supports streaming responses

AIAssistant

High-level interface for AI interactions
Manages chat history and context
Provides specialized methods for different use cases

ChatMessage

Data class representing chat messages
Supports different roles (user, assistant, system)

Examples
Simple Chat
pythonassistant = AIAssistant()
assistant.setup()
response = assistant.chat("Explain quantum computing")
Story Generation
pythonstory = assistant.generate_story("a robot learning emotions")
Code Review
pythoncode = "def factorial(n): return n * factorial(n-1) if n > 0 else 1"
review = assistant.code_review(code)
Available Models
The project works with any Ollama-compatible model. Popular options include:

llama3.2:3b - Fast, efficient model
llama3.2:1b - Lightweight option
codellama:7b - Specialized for code tasks
mistral:7b - Alternative general-purpose model

Configuration
You can customize the assistant by:

Changing the default model in AIAssistant.__init__()
Modifying the Ollama server URL in OllamaClient.__init__()
Adjusting streaming preferences in method calls

Error Handling
The project includes comprehensive error handling for:

Network connectivity issues
Model availability
API response errors
Streaming interruptions

Contributing
Feel free to submit issues and enhancement requests!
License
This project is open source and available under the MIT License.
Troubleshooting
Ollama not running: Ensure you've started the Ollama server with ollama serve
Model not found: The script will attempt to pull the model automatically, or you can manually run ollama pull <model-name>
Network errors: Check that Ollama is running on the default port (11434)
Memory issues: Try using a smaller model like llama3.2:1b for systems with limited RAM

**requirements.txt** - Copy this:
requests>=2.31.0
dataclasses>=0.8; python_version<"3.7"

**ai_assistant.py** - Copy the main code from the first artifact above

**examples/basic_usage.py** - Copy the example code from the last artifact above

