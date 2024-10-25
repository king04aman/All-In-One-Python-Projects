# Conversational Retrieval with LangChain and OpenAI

This directory contains a Python script that implements a conversational retrieval system using LangChain and OpenAI's API. The script allows users to query a collection of documents and receive responses based on the retrieved information.

## Features

- Load documents from a specified directory.
- Create and persist a vector store index for efficient querying.
- Engage in conversational interactions, maintaining chat history.
- Easily exit the program.

## Requirements

- Python 3.7+
- Required packages:
  - `openai`
  - `langchain`
  - `chromadb`

You can install the required packages using pip:

```bash
pip install openai langchain chromadb
```
## Setup
1. Clone the Repository:
    ```bash
    git clone https://github.com/king04aman/custom-gpt.git
    cd your_repository
    ```
2. Set the OpenAI API Key:
Replace `your_api_key_here` in the script with your actual OpenAI API key. You can also set the environment variable directly in your terminal:
    ```bash
    export OPENAI_API_KEY="your_api_key_here"
    ```
3. Prepare Your Data:
Place your documents in a folder named `data/`. The script will load all documents from this directory.

## Usage
Run the script from the command line:
```bash
python main.py
```
### Command Line Arguments
You can provide an initial query as a command line argument:
```bash
python main.py "Your initial query here"
```
### Interactive Mode
If no initial query is provided, the script will prompt you to enter queries interactively. Type your question and press Enter to get a response. Type `quit`, `q`, or exit to `exit` the program.

### Persistence
- Set the `PERSIST` variable to `True` in the script to enable saving the vector store index to disk for reuse in future sessions.
- The index will be saved in a directory named `persist/`.

## Example
```bash
Prompt (type 'quit' to exit): What is the significance of data persistence?
Response: [Your response here based on the documents]
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to submit issues or pull requests. Contributions are welcome!
