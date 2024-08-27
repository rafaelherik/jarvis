from setuptools import setup, find_packages


setup(
    name='jarvispy',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'google-generativeai',
    ],
    entry_points={
        'console_scripts': [
            'jarvis=jarvispy.main:start',  # Define the CLI command
            'jarvis-setup=jarvispy.main:setup',  # Command to update the API key
        ],
    },
    author='Rafael Herik de Carvalho',
    author_email='rafaelherik@gmail.com',
    description='A personal jarvispy powered by AI',
    python_requires='>=3.9',
)
