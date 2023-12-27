# Chat using Google Gemini API

import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from IPython.display import Markdown, display

from htmlTemplates import bot_template, css, user_template

# Access the variables using os.environ
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

# Set up model config
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}


# function to load Gemini Pro Model and get response
def get_gemini_response(input):
    model = genai.GenerativeModel(
        model_name="gemini-pro", generation_config=generation_config
    )
    chat = model.start_chat(history=[])
    response = chat.send_message(input)
    return response


def handle_user_input(input):
    try:
        response = get_gemini_response(input)
        if response:
            st.session_state["chat_history"].append(("You", input))
            st.subheader("Gemini:")
            for chunk in response:
                st.write(chunk.text)
            st.session_state["chat_history"].append(("Gemini", response.text))
        else:
            st.write("No output from Gemini")
    except Exception as e:
        st.write(f"An error occured: {str(e)}")


def main():
    # Load variables from the .env file
    load_dotenv()
    # Setup Streamlit UI
    st.set_page_config(
        page_title="Have a Chat with Gemini",
        page_icon=":books:",
        # layout="wide",
    )

    st.write(css, unsafe_allow_html=True)

    st.header("Chat with Gemini :books:")

    # Initialize session state for chat history if it doesn't exist
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    input = st.text_input("Ask any questions", key="input")

    submit = st.button("Ask the question")

    if submit and input:
        handle_user_input(input)
    st.subheader("The Chat History:")

    for i, message in enumerate(st.session_state["chat_history"]):
        # print(i, message)
        if i % 2 == 0:
            st.write(
                user_template.replace("{{MSG}}", message[1]),
                unsafe_allow_html=True,
            )
        else:
            st.write(
                bot_template.replace("{{MSG}}", message[1]),
                unsafe_allow_html=True,
            )


if __name__ == "__main__":
    main()
