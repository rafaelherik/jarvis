# Jarvis Assistant

Welcome to the Jarvis Assistant project! This is a basic implementation of a conversational assistant that leverages the power of generative AI to interact with users, answer questions, and perform basic actions. As this project evolves, it will continue to receive new functionalities and improvements.

## Features
- Conversational Abilities: Ask Jarvis questions or give commands, and it will respond with the best possible answer.
- Multiple Responses: When available, Jarvis can offer additional responses for you to choose from.
- Natural Language Processing: Utilizes the NLTK (Natural Language Toolkit) library for tokenization and part-of-speech tagging.
- Powered by Google Gemini: This assistant is powered by Google Gemini, Google's generative AI technology, enabling advanced content generation.


## Installation 

### Using PyPi
The package is not available yet

### Cloning the repo

#### Step 1: Clone the Repository
First, you'll need to clone the repository from GitHub to your local machine.

```bash copy
git clone https://github.com/rafaelherik/jarvis.git
cd jarvis
```

#### Step 2: Install the Required Build Tools
Before building the package, ensure you have the necessary tools installed. You’ll need setuptools and wheel, which are commonly used to build Python packages.

```bash copy
pip install setuptools wheel
```

#### Step 3: Build the Package
Once you are inside the cloned repository directory, you can build the package using the following command:

```bash copy
python setup.py sdist bdist_wheel
```

This command will generate distribution files (both source distribution and wheel) in the dist/ directory.

* **sdist** creates a source distribution (a .tar.gz file).
* **bdist_wheel** creates a wheel distribution (a .whl file).


#### Step 4: Install the Package Locally
Now that you have built the package, you can install it locally using pip:

- Installing from the Source Distribution (.tar.gz):

```bash copy
pip install dist/jarvispy-0.1.0.tar.gz
```

- Installing from the Wheel Distribution (.whl):

```bash copy
pip install dist/jarvispy-0.1.0-py3-none-any.whl
```

This will install the package and make it available in your Python environment.

#### Step 5: Verify Installation
You can verify that the package is installed correctly by running:

```bash copy
pip show jarvispy
```

This will display details about the installed package, confirming that it has been installed in your environment.


## Running the Assistant

Firt you must configure the Gemini API_KEY to use:

```bash copy
jarvis-setup
```


## Technologies Used

### Generative AI
This project is powered by Google Gemini, a cutting-edge generative AI model developed by Google. Google Gemini is designed to generate content and perform natural language understanding tasks, making it ideal for conversational AI applications.

### NLTK (Natural Language Toolkit)
The Natural Language Toolkit (NLTK) is a powerful Python library for working with human language data. In this project, NLTK is used for tokenizing user input and performing part-of-speech tagging, which helps the assistant understand the structure and meaning of your queries.

### Google Gemini
Google Gemini is a generative AI model developed by Google, known for its advanced language understanding and content generation capabilities. By integrating Google Gemini, Jarvis Assistant can provide high-quality responses to a wide range of queries, offering a state-of-the-art conversational experience.


### Contributing
As this project is under active development, contributions are welcome! Feel free to fork the repository, submit pull requests, or suggest new features by opening an issue.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.