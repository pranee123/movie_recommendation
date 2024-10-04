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
st.title("🎬Movie Recommender Systems")
user_input = st.text_input("Enter the Movie Title,Genre, Songs or Keyword👇")
demo_template = '''Based on your interest in "{user_input}", here are some personalized \
movie recommendations for you: Give me the popular songs from them and tell the story in short \
and recommend similar movies\
Enjoy your movie time! '''

template = PromptTemplate(input_variables=['user_input'],template=demo_template)

## Initiate the Model
llm = ChatGoogleGenerativeAI(model="gemini-pro",api_key=os.getenv("Google-Api-Key"))

if user_input:
    prompt = template.format(user_input=user_input)
    recommendations = llm.predict(text = prompt)
    st.write(f"Recommendations for You:\n{recommendations}")
else: 
    st.write("")





