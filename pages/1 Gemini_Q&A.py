# Question & Answers using Google Gemini API

import os
import textwrap

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from IPython.display import Markdown, display

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


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


# function to load Gemini Pro Model and get response
def get_gemini_response(question):
    model = genai.GenerativeModel(
        model_name="gemini-pro", generation_config=generation_config
    )
    response = model.generate_content(question, stream=True)
    return response


def handle_user_input(input):
    try:
        response = get_gemini_response(input)
        if response:
            st.subheader("Gemini:")
            for chunk in response:
                st.write(chunk.text)
        else:
            st.write("No output from Gemini")
    except Exception as e:
        st.write(f"An error occured: {str(e)}")


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
