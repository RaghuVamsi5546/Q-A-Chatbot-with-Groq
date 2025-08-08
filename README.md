# Simple Q/A Chatbot with Groq and Streamlit

This is a simple Q/A chatbot application built with **Streamlit** and the **Groq API**. It allows you to interact with various Groq language models to get answers to your questions.

-----

## How to Run

1.  **Clone the repository** and navigate to the project directory.
2.  **Install the required libraries** using `pip`:
    ```bash
    pip install streamlit langchain_groq langchain_core python-dotenv
    ```
3.  **Create a `.env` file** in the project directory and add your Groq API key:
    ```
    GROQ_API_KEY="your-api-key-here"
    ```
    Alternatively, you can enter your API key directly in the application sidebar.
4.  **Run the Streamlit application** from your terminal:
    ```bash
    streamlit run app.py
    ```

-----

## Features

  * **Interactive UI**: A simple and intuitive user interface built with Streamlit.
  * **Multiple Groq Models**: Choose from different Groq models like `gemma2-9b-it` and `llama-3.1-8b-instant`.
  * **Customizable Parameters**: Adjust the `temperature` and `max_tokens` to control the model's response style.
  * **API Key Management**: Securely enter your Groq API key in the sidebar.

-----
