import time
import google.generativeai as genai
import PIL.Image as pil
import streamlit as st
import datetime

API_KEY = 'YOUR_API_KEY'
genai.configure(api_key=API_KEY)

st.set_page_config(
    page_title="Gemini AI",
    layout="wide"
)


def greet_user():
    current_hour = datetime.datetime.now().hour

    if 5 <= current_hour < 12:
        greeting = "Good Morning!"
    elif 12 <= current_hour < 16:
        greeting = "Good Afternoon!"
    elif 16 <= current_hour < 21:
        greeting = "Good Evening!"
    else:
        greeting = "Good Night!"
    return greeting


st.header("Namaste, " + greet_user(), anchor=False, divider="violet")
with st.sidebar:
    st.image("./Google-Gemini-AI-Logo.png", use_column_width=True)
    st.write("")
    st.subheader("Welcome to the Gemini App! Feel free to explore and upload your files.")
    st.write("")
    st.markdown(":red[Disclaimer]")
    st.write("This app is powered by Google Gemini and has multilingual capabilities.")
    st.write("")
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg", "webp"])


def main():
    message_container = st.container(height=500, border=False)
    if uploaded_file is not None:
        message_container.image(pil.open(uploaded_file), use_column_width=True)
    if prompt := st.chat_input("Enter a prompt ", key="input-1"):
        message_container.subheader(":orange[User Prompt]")
        message_container.write(prompt)
        message_container.write("")
        start_time = time.time()
        if uploaded_file is not None:
            model = genai.GenerativeModel(model_name="gemini-pro-vision")
            image = pil.open(uploaded_file)

            with st.spinner("Generating response.."):
                response = model.generate_content([prompt, image])

        else:
            model = genai.GenerativeModel(model_name="gemini-pro")

            with st.spinner("Generating response.."):
                response = model.generate_content(prompt)
        st.sidebar.write("")
        message_container.subheader(":blue[Response]")
        st.sidebar.markdown(":green[Response Time: ]" + " {:.2f}".format(time.time() - start_time) + "s")
        message_container.write(response.text)


if __name__ == '__main__':
    main()
