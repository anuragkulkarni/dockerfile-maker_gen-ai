

# Dockerfile Generator

A Python script that generates optimized Dockerfiles for various programming languages using either a local LLM (Ollama) or an online LLM (Google Gemini). The tool follows Docker best practices, including multi-stage builds, and provides a clean, commented output.

## Features
- Supports multiple programming languages (e.g., Python, Node.js, Go).
- Generates Dockerfiles with:
  - Base image selection
  - Dependency installation
  - Working directory setup
  - Source code copying
  - Application runtime configuration
  - Multi-stage builds for efficiency
- Choose between offline (Ollama) or online (Google Gemini) LLM generation.
- Option to save the generated Dockerfile to disk.

## Prerequisites
- **Python 3.9+**: Ensure Python is installed and added to your PATH.
- **Ollama**: For offline mode, install Ollama and pull the `llama3.2:1b` model.
- **Google API Key**: For online mode, obtain a Google Generative AI API key.

## Installation

1. **Clone the Repository** (if hosted on GitHub):
   ```bash
   git clone https://github.com/yourusername/dockerfile-generator.git
   cd dockerfile-generator
   ```

2. **Install Dependencies**:
   ```bash
   pip install ollama google-generativeai
   ```

3. **Set Up Ollama (Offline Mode)**:
   - Install Ollama: [Ollama Installation Guide](https://ollama.ai/)
   - Pull the model:
     ```bash
     ollama pull llama3.2:1b
     ```
   - Start the Ollama server:
     ```bash
     ollama serve
     ```

4. **Set Up Google API Key (Online Mode)**:
   - Obtain an API key from [Google Cloud](https://cloud.google.com/).
   - Set it as an environment variable:
     ```bash
     # Windows CMD
     set GOOGLE_API_KEY=your_api_key_here
     # Or add to your .env file
     ```

## Usage

1. **Run the Script**:
   ```bash
   python docker_creator.py
   ```

2. **Follow the Prompts**:
   - Enter the programming language (e.g., `python`, `node`, `go`).
   - Choose the LLM option:
     - `offline`: Uses local Ollama LLM.
     - `online`: Uses Google Gemini LLM.
   - View the generated Dockerfile.
   - Optionally save it as `Dockerfile` in the current directory.

### Example
```bash
$ python docker_creator.py
Enter the programming language: python
Choose the LLM option (online/offline): online
Generating Dockerfile using Google LLM...

Generated Dockerfile:
# Build stage
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY . .
CMD ["python", "main.py"]

Dockerfile generated successfully.
Do you want to save the Dockerfile? (yes/no): yes
Dockerfile saved successfully as 'Dockerfile'.
```

## File Structure
```
dockerfile-generator/
├── docker_creator.py  # Main script
├── README.md          # This file
└── Dockerfile         # Generated output (if saved)
```

## Notes
- Ensure Ollama is running locally if using `offline` mode.
- The Google API key must be set for `online` mode to work.
- The generated Dockerfile assumes a basic project structure (e.g., `requirements.txt` for Python). Adjust your project files accordingly.

## Troubleshooting
- **ModuleNotFoundError**: Run `pip install ollama google-generativeai`.
- **Ollama Connection Error**: Start the Ollama server with `ollama serve`.
- **Google API Error**: Verify your `GOOGLE_API_KEY` is set correctly.
- **Unexpected Output**: The LLM might occasionally generate imperfect Dockerfiles. Check the output and adjust manually if needed.

## Contributing
Feel free to submit issues or pull requests to improve the script, add support for more languages, or enhance the prompt for better LLM output.


