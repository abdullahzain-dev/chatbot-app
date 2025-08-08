# app.py
import streamlit as st
import requests

st.title("💬 Chatbot (OpenRouter)")
st.caption("Powered by openrouter.ai")

api_key = "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"

# Store chat history in Streamlit session
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Say something...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send to OpenRouter API
    headers = {
        "Authorization": f"Bearer {api_key}",
        "HTTP-Referer": "https://yourdomain.com",
        "X-Title": "streamlit-chat",
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": st.session_state.messages,
        "temperature": 0.7,
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        reply = response.json()["choices"][0]["message"]["content"]
    else:
        reply = "Error: " + response.text

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)






