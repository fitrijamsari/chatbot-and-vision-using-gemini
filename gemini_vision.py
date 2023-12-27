import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from IPython.display import Markdown, display
from PIL import Image

# Access the variables using os.environ
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

# Set up model config
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 4096,
}


# function to load Gemini Pro Model and get response
def get_gemini_response(input, image):
    model = genai.GenerativeModel(
        model_name="gemini-pro-vision", generation_config=generation_config
    )
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text


def handle_user_input(input, image):
    try:
        response = get_gemini_response(input, image)
        if response:
            st.subheader("Gemini Vision Response:")
            st.write(response)
        else:
            st.write("No output from Gemini")
    except Exception as e:
        st.write(f"An error occured: {str(e)}")


def main():
    # Load variables from the .env file
    load_dotenv()
    # Setup Streamlit UI
    st.set_page_config(
        page_title="Gemini Image Demo",
        page_icon=":frame_with_picture:",
        # layout="wide",
    )

    st.header("Gemini Pro Vision Application")

    user_question = st.text_input(
        "Ask Any Question About the Image to Gemini :frame_with_picture: ", key="input"
    )

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    image = ""
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Tell me about the image")

    ## If ask button is clicked
    if submit:
        handle_user_input(user_question, image)


if __name__ == "__main__":
    main()
