import pickle
from preprocess import clean_text
import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

#Load Model
#Set Gemini Api

load_dotenv()
genai.configure(api_key = os.getenv('GEMINI_API_KEY'))



with open('sentiment.pkl', 'rb') as file:
    model_svc = pickle.load(file)

with open('transformer.pkl', 'rb') as file:
    embed_model = pickle.load(file)

#Prediction Test

def predict(text):
    processed_text = clean_text(text)
    vectorized_text = embed_model.encode([processed_text])
    prediction = model_svc.predict(vectorized_text)[0]
    sentiment_map = {1: 'Positive', -1: 'Negative', 0: 'Neutral'}
    return sentiment_map.get(prediction, 'Unknown')

def gemini_predict(text):
    model = genai.GenerativeModel('models/gemini-2.5-pro')
    prompt = f'Analyze the financial news predicted with Positive/Negative/Neutral {text}'
    response = model.generate_content(prompt)
    return response.text.strip()

# UI

st.title('Financial News Analysis')
st.subheader('Sentiment Analysis using GenAI')

# User_input

user_input = st.text_area("Enter the news: ")

if st.button('Analyze Sentiment'):
    if user_input.strip():
        sentiment = predict(user_input)
        sentiment_gemini = gemini_predict(user_input)

        st.success(f"Predicted Sentiment: {sentiment}")
        st.info(f"Predicted Sentiment: {sentiment_gemini}")
    else:
        st.warning('Enter the valid text.')






