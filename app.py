import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="SDG Chatbot", page_icon="💬", layout="centered")

st.title("SDG Chatbot (Dialogflow + Streamlit)")
st.caption("Embeds the official Dialogflow Messenger web component.")

# --- Sidebar controls (you can hardcode these if you want) ---
with st.sidebar:
    st.header("Dialogflow Settings")
    agent_id = st.text_input(
        "Agent ID",
        value="a298d9eb-3468-4c05-9b07-26b59db74a5d",
        help="Copy from Dialogflow Console → Agent settings.",
    )
    chat_title = st.text_input("Chat Title", value="sdg")
    language_code = st.text_input("Language Code", value="en")

    st.markdown("---")
    st.subheader("Theme")
    user_bubble = st.color_picker("User bubble", "#2563eb")
    bot_bubble = st.color_picker("Bot bubble", "#f1f5f9")
    header_bg = st.color_picker("Header background", "#0ea5e9")
    text_color = st.color_picker("Text color", "#0f172a")

st.write("Click the launcher at the bottom-right to start chatting.")

# --- Build the HTML snippet that injects Dialogflow Messenger ---
html_snippet = f"""
  <style>
    :root {{
      --df-messenger-font-color: {text_color};
      --df-messenger-chat-background: #ffffff;
      --df-messenger-message-user: {user_bubble};
      --df-messenger-message-bot: {bot_bubble};
      --df-messenger-input-box-color: #ffffff;
      --df-messenger-input-font-color: {text_color};
      --df-messenger-send-icon: {user_bubble};
      --df-messenger-button-titlebar-color: {header_bg};
      --df-messenger-button-titlebar-font-color: #ffffff;
      --df-messenger-chat-border-radius: 16px;
    }}
    body {{ background: transparent; }}
  </style>

  <!-- Dialogflow Messenger bootstrap -->
  <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>

  <!-- Dialogflow Messenger Web Component -->
  <df-messenger
    intent="WELCOME"
    chat-title="{chat_title}"
    agent-id="{agent_id}"
    language-code="{language_code}"
  >
    <df-messenger-chat-bubble chat-title="{chat_title}"></df-messenger-chat-bubble>
  </df-messenger>
"""

# Render with enough height so the launcher is visible
html(html_snippet, height=640, scrolling=True)

# --- Troubleshooting tips (shown in the app) ---
with st.expander("Troubleshooting"):
    st.markdown(
        """
**If the widget doesn't show up:**
1. Add your deployment domain(s) to **Dialogflow → Agent settings → Authorized domains**. For Streamlit Cloud, add:
   - `streamlit.app`
   - `*.streamlit.app`
   - your exact app subdomain (e.g., `your-app-name.streamlit.app`)
2. Verify the **Agent ID** above is correct.
3. Hard refresh the page (Ctrl/Cmd+Shift+R) and temporarily disable ad/script blockers.
4. Open **DevTools → Console** and check for red errors (CORS, CSP, blocked script).
        """
    )
