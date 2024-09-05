from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# Configure the new model
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Use the updated model
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text, image):
    if input_text:
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)   
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input_text = st.text_input("Input Prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    submit = st.button("Tell me about the image")

    if submit:
        response = get_gemini_response(input_text, image)
        st.subheader("The response is")
        st.write(response)
