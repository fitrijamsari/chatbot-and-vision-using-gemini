import pandas as pd
import streamlit as st

# Page Title
st.title("Google's Gemini Model Guide 🚀🤖")

# Introduction to Google Gemini
st.header("Introduction to Google Gemini")
st.write(
    """
Google Gemini is a multimodal large language model (LLM) capable of understanding different types of information, including text, audio, images, and video. It consists of Gemini Ultra, Gemini Pro, and Gemini Nano. Announced on December 6, 2023, Google positions Gemini as a strong competitor to OpenAI's GPT-4, claiming it to be their most capable and general-purpose AI model.

Gemini Pro Availability
"""
)
st.write(
    """
Google has made Gemini Pro, a language model designed for developers, available worldwide. Developers can access Google AI Studio, a free tool enabling them to explore Gemini's capabilities and integrate it into their applications.
"""
)

# Additional Language Support
st.write(
    """
Additional Language Support
"""
)
st.write(
    """
Gemini now supports six additional languages: Hindi, Japanese, Korean, Portuguese, Chinese, and Spanish. Google plans to expand language support to more languages in early 2024.
"""
)

# Learn More section
st.header("Learn More")
# Add a clickable link
st.markdown(
    """
Try and clone my repositories to test the features [git repositories](https://github.com/fitrijamsari/chatbot-and-vision-using-gemini.git).
""",
    unsafe_allow_html=True,
)
