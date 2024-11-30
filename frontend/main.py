import streamlit as st
from backend.sklearn_llm import run_llm
import openai

def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            ("assistant", "Hi! I'm here to help you with Scikit-Learn documentation. What would you like to know?")
        ]

def validate_openai_key(api_key):
    """Validate the OpenAI API key by making a simple request"""
    client = openai.OpenAI(api_key=api_key)
    try:
        client.models.list()
    except openai.AuthenticationError:
        return False
    else:
        return True

def main():
    st.set_page_config(
        page_title="Chat with Scikit-Learn docs",
        page_icon="📚",
        layout="centered"
    )
    st.title("Chat with Scikit-Learn docs")

    initialize_session_state()

    openai_api_key = st.text_input("OpenAI API Key", type="password")

    if not openai_api_key:
        st.warning("Please enter your OpenAI API Key to start chatting.")
        return
    
    if not validate_openai_key(openai_api_key):
        st.error("Invalid OpenAI API Key. Please enter a valid key.")
        return

    for msg in st.session_state.messages:
        with st.chat_message(msg[0]):
            st.write(msg[1])
    
    if prompt := st.chat_input("Ask a question about Scikit-Learn"):
        st.session_state.messages.append(("user", prompt))
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # No need to format history - it's already in the right format
                answer = run_llm(prompt, st.session_state.messages[:-1], openai_key=openai_api_key)  # Exclude current message
                st.write(answer)

        st.session_state.messages.append(("assistant", answer))

if __name__ == "__main__":
    main()

