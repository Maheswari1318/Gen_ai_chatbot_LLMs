import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Gemini AI Chatbot", page_icon="🤖")

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("API key missing")
    st.stop()

client = genai.Client(api_key=GOOGLE_API_KEY)

st.title("🤖 Gemini Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask Gemini...")

if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    reply = response.text

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.history.append({"role": "assistant", "content": reply})
