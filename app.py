import streamlit as st
from g4f.client import Client
import g4f

# Initialize the G4F client
client = Client()

# Define the function for generating creative writing prompts
def generate_writing_prompt(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
    )
    return response.choices[0].message.content

# Streamlit user interface
def main():
    st.title("The Next Generation AI Chatbot")
    st.write("Unleash your creativity! Get inspired with unique story ideas, prompts, and plot twists.")
    
    user_input = st.text_area("Enter a genre, tone, or initial plot point...", height=150)
    generate_button = st.button("Generate Answer")
    # chat_button = st.button("Chat with Assistant")
    
    if generate_button:
        if user_input:
            prompt = generate_writing_prompt(user_input)
            st.write("### Generated Prompt")
            st.write(prompt)
        else:
            st.error("Please enter some input to generate a prompt.")
    
    # if chat_button:
    #     st.write("### Assistant Chat")
    #     st.write("This feature is under development.")

if __name__ == "__main__":
    main()
