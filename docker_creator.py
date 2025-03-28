import ollama

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

def generate_dockerfile(language):
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

if __name__ == "__main__":
    language = input("Enter the programming language: ")
    print("Generating Dockerfile...")
    dockerfile = generate_dockerfile(language)
    print(dockerfile)
    print("Dockerfile generated successfully.")
    save_option = input("Do you want to save the Dockerfile? (yes/no): ").strip().lower()
    if save_option == "yes":
        with open("Dockerfile", "w") as file:
            file.write(dockerfile)
        print("Dockerfile saved successfully as 'Dockerfile'.")
    else:
        print("Skipping save operation.")
