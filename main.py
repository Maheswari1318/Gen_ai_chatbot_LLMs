import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered",
)

# Get API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Load Gemini model
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("models/gemini-1.5-flash")
# Initialize chat session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Title
st.title("🤖 Gemini Pro - ChatBot")

# Function to convert Gemini role to Streamlit role
def translate_role_for_streamlit(role):
    if role == "model":
        return "assistant"
    return role

# Display chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Chat input
user_prompt = st.chat_input("Ask Gemini...")

if user_prompt:
    # Show user message
    st.chat_message("user").markdown(user_prompt)

    # Send message to Gemini
    response = st.session_state.chat_session.send_message(user_prompt)

    # Show Gemini response
    with st.chat_message("assistant"):
        st.markdown(response.text)
