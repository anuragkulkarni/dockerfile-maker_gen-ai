import ollama
import google.generativeai as genai
import os
Prompt = """
ONLY Generate an ideal dockerfile for {language} with best practices and comments in docker file. Do not provide any description
INCLUDE:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
- Multi-stage docker build
"""

def generate_via_local_llm_dockerfile(language):
    response = ollama.chat(model="llama3.2:1b", messages=[{"role": "user", "content": Prompt.format(language=language)}])
    # Get the raw content and remove triple backticks if present
    dockerfile_content = response['message']['content']
    # Strip ``` from the beginning and end, if they exist
    if dockerfile_content.startswith("```"):
        dockerfile_content = dockerfile_content[3:]
    if dockerfile_content.endswith("```"):
        dockerfile_content = dockerfile_content[:-3]
    # Remove any remaining "```language" lines (e.g., ```dockerfile) and trim whitespace
    dockerfile_content = "\n".join(line for line in dockerfile_content.splitlines() if not line.strip().startswith("```"))
    return dockerfile_content.strip()

def generate_via_google_llm_dockerfile(language):
        # Set your API key here
        os.environ["GOOGLE_API_KEY"] = "YOUR-GOOGLE-API-KEY"
       # Configure the Gemini model
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(Prompt.format(language=language))
        dockerfile_content = response.text  # Access the text content
        # Strip ``` from the beginning and end, if present
        if dockerfile_content.startswith("```"):
            dockerfile_content = dockerfile_content[3:]
        if dockerfile_content.endswith("```"):
            dockerfile_content = dockerfile_content[:-3]
        lines = [line for line in dockerfile_content.splitlines() if line.strip() and not line.strip().startswith("```")]
        # Remove any leading line that might be a label like "dockerfile"
        if lines and lines[0].strip().lower() == "dockerfile":
            lines = lines[1:]
        # Remove any ```language lines and trim whitespace
        dockerfile_content = "\n".join(line for line in dockerfile_content.splitlines() if not line.strip().startswith("```"))
        return dockerfile_content.strip()


if __name__ == "__main__":
    language = input("Enter the programming language: ")
    option = input("Choose the LLM option (online/offline): ").strip().lower()
    if option=="offline":
        print("Generating Dockerfile using local LLM...")
        dockerfile = generate_via_local_llm_dockerfile(language)
    else:
        print("Generating Dockerfile using Google LLM...")
        dockerfile = generate_via_google_llm_dockerfile(language)
    print("Generating Dockerfile...")
    print(dockerfile)
    print("Dockerfile generated successfully.")
    save_option = input("Do you want to save the Dockerfile? (yes/no): ").strip().lower()
    if save_option == "yes":
        with open("Dockerfile", "w") as file:
            file.write(dockerfile)
        print("Dockerfile saved successfully as 'Dockerfile'.")
    else:
        print("Skipping save operation.")












