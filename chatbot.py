from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

st.title("LANGCHAIN OPENAI")
input_text=st.text_input("Search the topic you want")

llm=Ollama(model="llama2")
output=StrOutputParser()
chain=prompt|llm|output

if input_text:
    st.write(chain.invoke({'question':input_text}))