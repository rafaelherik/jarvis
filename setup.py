from setuptools import setup, find_packages
import os


def setup_api_key():
    config_dir = os.path.join(os.path.expanduser("~"), ".jarvis_assistant")
    config_file = os.path.join(config_dir, "config.txt")

    # Create the directory if it doesn't exist
    os.makedirs(config_dir, exist_ok=True)

    # Prompt the user for the API Key
    api_key = input("Please enter your Google Gemini API_KEY (See how to get the key on https://ai.google.dev/gemini-api): ")

    if api_key is not None and api_key != "":
        # Save the API Key to a config file
        with open(config_file, "w") as f:
            f.write(f"API_KEY={api_key}\n")

        print(f"API Key saved to {config_file}")
    else:
        print(f"API Key not informed use the Environment Variable JARVIS_GEMINI_API_KEY to store the api key.")


setup(
    name='jarvis_assistant',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'google-generativeai',
    ],
    entry_points={
        'console_scripts': [
            'jarvis=jarvis_ai_assistant.main:start',  # Define the CLI command
            'jarvis-setup=jarvis_ai_assistant.main:setup',  # Command to update the API key
        ],
    },
    author='Rafael Herik de Carvalho',
    author_email='rafaelherik@gmail.com',
    description='A personal jarvis_assistant powered by AI',
    python_requires='>=3.9',
)
