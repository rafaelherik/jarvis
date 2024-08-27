from jarvispy.assistant import wakeup_assistant
import os

def start():
    wakeup_assistant()

def setup():
    setup_api_key()

def setup_api_key():
    config_dir = os.path.join(os.path.expanduser("~"), ".jarvispy")
    config_file = os.path.join(config_dir, "config.txt")

    # Create the directory if it doesn't exist
    os.makedirs(config_dir, exist_ok=True)

    # Prompt the user for the API Key
    api_key = input("Please enter your Google Gemini API_KEY: ")

    # Save the API Key to a config file
    with open(config_file, "w") as f:
        f.write(f"API_KEY={api_key}\n")

    print(f"API Key saved to {config_file}")

if __name__ == "__main__":
    start()