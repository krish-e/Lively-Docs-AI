# Lively Docs AI

Lively Docs AI is a Command Line Interface (CLI) tool designed to enhance document understanding through AI-powered question answering. With this tool, users can upload PDF documents either from their local machine or directly from online sources. Once uploaded, they can ask questions related to the content of the document, and the AI model, powered by OpenAI API, will generate answers using Langchain's Retrieval Augmented Generation(RAG) framework.

## Features

- **PDF Upload:** Easily upload PDF documents from local files or online sources(Except Google Drive).
- **Question Answering:** Ask questions related to the document content.
- **AI-powered Responses:** Utilizes OpenAI API to generate accurate answers using the RAG framework.
- **Document Understanding:** Enhances comprehension and information extraction from documents.

## Requirements

- Python 3.5 or above
- OpenAI API Key ([Get here](https://platform.openai.com/api-keys))
- Internet Connection(for online PDF sources)

## Installation

1. Clone the repository:
  
    ```bash
    git clone https://github.com/krish-e/Lively-Docs-AI.git

2. Navigate to the project directory:
    ```bash
    cd Lively-Docs-AI

3. Install dependencies:
    ```bash
    pip install -r requirements.txt


## Usage
1. Run the CLI tool:
    ```bash
    python app.py

3. Give URL of a document local or online source(except Google Drive) when prompted
4. Ask questions related to the document content.
5. Receive AI-generated answers.


## Credits

Special thanks to OpenAI and Langchain for providing the powerful AI models and super simple frameworks used in this project.





