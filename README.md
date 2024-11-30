# Scikit-Learn RAG Chatbot

This project is a chatbot application that leverages Retrieval-Augmented Generation (RAG) in LangChain to interact with the documentation of Scikit-Learn. The chatbot is designed to provide users with accurate and contextually relevant information from the Scikit-Learn documentation.

## Features

- **RAG Integration**: Utilizes Retrieval-Augmented Generation to enhance the chatbot's ability to provide precise answers by retrieving relevant documents and generating responses based on them.
- **LangChain Framework**: Built using the LangChain framework to streamline the development of the chatbot.
- **Scikit-Learn Documentation**: Focuses on providing information from the Scikit-Learn documentation, making it a valuable tool for data scientists and machine learning practitioners.
- **[Streamlit App](https://skearnrag-kendkjjwdl4pzn2n2psrwp.streamlit.app/)**: The application is deployed on Streamlit Community Cloud, ensuring easy access and a user-friendly interface.

## Getting Started

To get started with the Scikit-Learn RAG Chatbot, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/martinijfb/sklearn_RAG.git
    cd sklearn_RAG
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    streamlit run frontend/main.py
    ```

## Usage

Once the application is running, you can interact with the chatbot through the Streamlit interface. Simply type your questions related to Scikit-Learn, and the chatbot will provide responses based on the documentation.

### API Key

To use the chatbot, you need to provide an OpenAI API key directly in the Streamlit app interface. When you launch the app, you will be prompted to enter your API key. Make sure to use a valid OpenAI API key to enable the chatbot functionality.
