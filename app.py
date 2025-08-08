import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT_NAME'] = "Q/A chatbot with GROQ"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user query."),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, api_key, model_name, temperature, max_tokens):
    if not api_key:
        return "Please enter your Groq API key in the sidebar."

    output_parser = StrOutputParser()
    llm = ChatGroq(
        model=model_name,
        groq_api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens
    )
    chain = prompt | llm | output_parser
    return chain.invoke({"question": question})

st.title("Q/A Chatbot with GROQ")
st.sidebar.title("Settings")

api_key = st.sidebar.text_input("Enter your Groq API key:", type="password")
model_name = st.sidebar.selectbox(
    "Select a Groq model",
    ['gemma2-9b-it', 'llama-3.1-8b-instant', 'meta-llama/llama-guard-4-12b', 'whisper-large-v3']
)
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=100)

user_input = st.text_input("You: Ask your Query", placeholder="Type your question here...")

if user_input:
    with st.spinner("Generating response..."):
        response = generate_response(user_input, api_key, model_name, temperature, max_tokens)
    st.write("Answer:", response)
else:
    st.write("Please enter your Groq API key and ask a question.")