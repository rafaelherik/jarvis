import os
from datetime import datetime
import nltk
import google.generativeai as genai
import contextlib


def setup_assistant():
    """Run this function only during the setup phase to download required NLTK data."""
    print("Setting up Jarvis Assistant... Downloading NLTK data...")
    with contextlib.redirect_stdout(open(os.devnull, "w")):
        nltk.download('punkt', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
        nltk.download('averaged_perceptron_tagger_eng', quiet=True)
   

setup_assistant()


def load_api_key():
    config_dir = os.path.join(os.path.expanduser("~"), ".jarvispy")
    config_file = os.path.join(config_dir, "config.txt")

    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            for line in f:
                if line.startswith("API_KEY"):
                    return line.split("=")[1].strip()

    else:
        key = os.environ.get("JARVIS_GEMINI_API_KEY")
        if key is not None:
            return key
    return None


def query_gemini_api(model, question):
    response = model.generate_content(question)

    # Save the candidates and return the best one (first one)
    candidates = response.candidates
    if candidates:
        return candidates, candidates[0].content.parts[0].text
    else:
        return None, "Sorry, I couldn't generate a response."


def is_question(user_input):
    # Check for question marks or common question words
    question_words = ["what", "how", "why", "when", "where", "who", "is", "are", "do", "does", "can", "could", "would",
                      "should"]

    # Tokenize the input and check for question words
    tokens = nltk.word_tokenize(user_input.lower())
    if "?" in user_input or tokens[0] in question_words:
        return True
    return False


def is_action(user_input):
    # Tokenize and part-of-speech tagging to detect verbs (commands)
    tokens = nltk.word_tokenize(user_input)
    tagged = nltk.pos_tag(tokens)

    # Check for verbs (VB, VBP, VBZ)
    for word, pos in tagged:
        if pos in ["VB", "VBP", "VBZ"]:  # Verb, base form, or third-person singular
            return True
    return False


def get_greeting():
    current_time = datetime.now().time()
    morning_start = datetime.strptime("06:00", "%H:%M").time()
    afternoon_start = datetime.strptime("12:00", "%H:%M").time()
    evening_start = datetime.strptime("18:00", "%H:%M").time()
    if morning_start <= current_time < afternoon_start:
        return "Good Morning!"
    elif afternoon_start <= current_time < evening_start:
        return "Good Afternoon!"
    else:
        return "Good Evening!"


def wakeup_assistant():
    # Print the greeting
    greeting = get_greeting()
    print(greeting)

    api_key = load_api_key()

    if not api_key:
        print("API Key not found. Please set up your API Key using 'jarvis setup'.")
        exit(1)

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')

    # Provide instructions on how to interact with the jarvis_assistant
    print("\nWelcome! I'm your jarvis_assistant. Here’s how you can interact with me:")
    print("1. You can ask me questions (e.g., 'What is the weather today?').")
    print("2. You can give me commands (e.g., 'Add project context').")
    print("3. If you want to exit, simply type 'exit' or 'quit'.")
    print("\nHow can I assist you today?\n")

    while True:
        user_input = input("You: ")
        if "exit" in user_input.lower() or "quit" in user_input.lower():
            print("Goodbye!")
            break
        response = handle_input(model, user_input)
        print(f"Jarvis: {response}")


def handle_input(model, user_input):
    tokens = nltk.word_tokenize(user_input)
    tagged = nltk.pos_tag(tokens)

    # Construct a more informative prompt based on token analysis
    nouns = [word for word, pos in tagged if pos.startswith('NN')]
    verbs = [word for word, pos in tagged if pos.startswith('VB')]

    # Create a context-aware prompt
    prompt = f"User input: {user_input}. "
    if nouns:
        prompt += f"The main topics are: {', '.join(nouns)}. "
    if verbs:
        prompt += f"The key actions are: {', '.join(verbs)}. "

    if is_question(user_input):
        candidates, best_response = query_gemini_api(model, prompt)
        if candidates:
            current_index = 0
            print(f"Jarvis: {best_response}")

            # Offer the user to see the next candidate if available
            while current_index < len(candidates) - 1:
                user_decision = input("Would you like to see another response? (yes/no): ").strip().lower()
                if user_decision == "yes":
                    current_index += 1
                    print(f"Jarvis: {candidates[current_index].content.parts[0].text}")
                else:
                    break
            return "That's all the responses I have for that query. Can I help you with something else?"
        else:
            return best_response
    elif is_action(user_input):
        return "That seems like an action. I'll get right on it!"
    elif "exit" in user_input.lower() or "quit" in user_input.lower():
        return "Goodbye!"
    else:
        return "I'm here to assist! How can I help you?"
