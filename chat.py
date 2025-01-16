import streamlit as st
import google.generativeai as genai

# Configure Google Generative AI
API_KEY = "AIzaSyDfddsgyzfuVy0jxhMtUsm1CGpGFwrcih4"
genai.configure(api_key=API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel(model_name="gemini-pro")

# Streamlit App
st.title("Chat With AI")
st.write("Type 'stop' to end the chat.")

# Session State to Store Chat History
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat()
    st.session_state.messages = []  # To store chat history

# Chat Interface
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("You: ", placeholder="Type your message here...")
    submitted = st.form_submit_button("Send")

# Process User Input
if submitted and user_input:
    if user_input.lower() == "stop":
        st.success("Chat ended. Thank you!")
    else:
        # Get Response from Generative AI
        response = st.session_state.chat.send_message(user_input)

        # Store Messages in Session State
        st.session_state.messages.append(("You", user_input))
        st.session_state.messages.append(("Bot", response.text))

# Display Chat History
if st.session_state.messages:
    st.write("### Chat History")
    for sender, message in reversed(st.session_state.messages):  # Reverse the order
        if sender == "You":
            st.write(f"**{sender}:** {message}")
        else:
            st.write(f"**{sender}:** {message}")



