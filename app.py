import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Chatbot", page_icon="💬", layout="centered")

# --- Build clean Dialogflow Messenger snippet ---
html_snippet = """
  <style>
    :root {
      --df-messenger-font-color: #000000;
      --df-messenger-chat-background: #ffffff;
      --df-messenger-message-user: #2563eb;
      --df-messenger-message-bot: #f1f5f9;
      --df-messenger-input-box-color: #ffffff;
      --df-messenger-input-font-color: #000000;
      --df-messenger-send-icon: #2563eb;
      --df-messenger-button-titlebar-color: #2563eb;
      --df-messenger-button-titlebar-font-color: #ffffff;
      --df-messenger-chat-border-radius: 16px;
    }
    body { background: #111827; }
  </style>

  <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
  <df-messenger
    intent="WELCOME"
    chat-title="SDG"
    agent-id="a298d9eb-3468-4c05-9b07-26b59db74a5d"
    language-code="en"
  >
    <df-messenger-chat-bubble chat-title="SDG"></df-messenger-chat-bubble>
  </df-messenger>
"""

# --- Render chatbot fullscreen-like ---
st.markdown("<h3 style='text-align:center;'>SDG Chatbot</h3>", unsafe_allow_html=True)
html(html_snippet, height=700, scrolling=True)
