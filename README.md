
# Gemini Chat

Welcome to Gemini Chat, a conversational AI chatbot powered by Google Gemini API and built with Streamlit. This chatbot leverages the advanced capabilities of Google's generative models to provide intelligent responses to user prompts, including support for image inputs.

![image](https://github.com/user-attachments/assets/fd6fb8eb-59f8-49e0-9751-17f67302022c)


## Features

- **Multilingual Support**: Capable of understanding and generating content in multiple languages.
- **Image Upload**: Allows users to upload images for more context-aware responses.
- **Real-time Response**: Displays response time for each query.

## Setup

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Google Generative AI (gemini)
- Pillow

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/YashasJKumar/Gemini_Chat.git
    cd Gemini_Chat
    ```

2. Install the required packages:

    ```sh
    pip install streamlit google-generativeai pillow
    ```

3. Add your Google Gemini API key:

    Replace `API_KEY = 'YOUR_API_KEY'` in the code with your own API key.

4. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

## Usage

- **Sidebar**: You can upload an image using the sidebar.
- **Chat Input**: Enter your prompt in the chat input box.
- **Response**: The chatbot will generate a response, which will be displayed along with the response time.

## Snapshot

<img width="1469" alt="Screenshot 2024-07-30 at 7 20 15 AM" src="https://github.com/user-attachments/assets/52b7ff63-ce98-4dc2-b422-c41c6e53fefa">


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Acknowledgements

- Google Gemini API
- Streamlit
- Pillow
