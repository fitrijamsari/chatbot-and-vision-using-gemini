import os
import pathlib
import textwrap

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from IPython.display import Markdown, display

# Access the variables using os.environ
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


# function to load Gemini Pro Model and get response
def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text


def handle_user_input(input):
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)


def main():
    # Load variables from the .env file
    load_dotenv()
    # Setup Streamlit UI
    st.set_page_config(
        page_title="Ask Any Question to Gemini",
        page_icon=":books:",
        # layout="wide",
    )

    st.header("Ask Any Question to Gemini :books:")

    user_question = st.text_input(
        "Ask any questions",
    )
    if user_question:
        handle_user_input(user_question)


if __name__ == "__main__":
    main()
