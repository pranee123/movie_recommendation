# Importing the libraries
import streamlit as st
import google.generativeai as genai
from langchain import PromptTemplate,LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

# Set Up THe Local Environment
import os
from dotenv import load_dotenv
load_dotenv() # Activate the Local Environment
genai.configure(api_key=os.getenv("Google-Api-Key"))

# Designing the Webpage...
st.title("👀Movie Recommender Systems")
user_input = st.text_input("Enter the Movie Title,Genere, songs or Keyword👇")
demo_template = '''Based on {user_input} give me Movie Recommendations and sort \
the recommendations by geners, movie songs {user_input}'''

template = PromptTemplate(input_variables=['user_input'],template=demo_template)

## Initiate the Model
llm = ChatGoogleGenerativeAI(model="gemini-pro",api_key=os.getenv("Google-Api-Key"))

if user_input:
    prompt = template.format(user_input=user_input)
    recommendations = llm.predict(text = prompt)
    st.write(f"Recommendations for You:\n{recommendations}")
else: 
    st.write("")


