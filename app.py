import streamlit as st
from g4f.client import Client
import openai

# API Key should be secured and not exposed in the script
openai.api_key = st.secrets["AIzaSyC3BAuvhsr96v9FN1HKPmMoAMUcTYfcwFM"]
client = Client()

def generate_writing_prompt(user_input, model_version="gpt-3.5-turbo", max_tokens=150):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
        language="en",  # Default language to English
        max_tokens=max_tokens
    )
    return response.choices[0].message.content

def main():
    st.title("The Next Generation AI Chatbot")
    st.write("Unleash your creativity! Get inspired with unique story ideas, prompts, and plot twists.")
    
    user_input = st.text_area("Enter a genre, tone, or initial plot point...", height=150)
    model_version = st.selectbox("Choose the model version", ["gpt-3.5-turbo", "gpt-4"], index=1)
    max_tokens = st.slider("Select the length of the prompt", 50, 300, 150)
    
    generate_button = st.button("Generate Answer")
    
    if generate_button:
        if user_input:
            prompt = generate_writing_prompt(user_input, model_version=model_version, max_tokens=max_tokens)
            st.write("### Generated Prompt")
            st.write(prompt)
        else:
            st.error("Please enter some input to generate a prompt.")

if __name__ == "__main__":
    main()
