
**Talk to Me: An AI-Powered Conversational Chatbot with Voice Input and Output**

**Description:**

This project demonstrates how to build an interactive conversational chatbot using Streamlit, OpenAI, and other Python libraries. The chatbot allows you to communicate using both text and voice, providing a more engaging and natural user experience.  It leverages OpenAI's language models for understanding and generating human-like text, as well as their speech-to-text and text-to-speech capabilities for seamless voice interaction.

**Installation:**

1. **Create a virtual environment (optional but recommended):**

   ```bash
   conda create -n chatbot python=3.9 
   conda activate chatbot
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

**Execution Flow:**

1. **Initialization:**
   - The app initializes by setting up the session state to store conversation history.
   - An initial welcome message from the assistant is added to the chat.

2. **Voice Input:**
   - The `audio_recorder` component captures audio input from the user's microphone.
   - The recorded audio is temporarily saved to a file.
   - The `speech_to_text` function (using OpenAI's Whisper API) transcribes the audio into text.
   - The transcribed text is added as a user message to the conversation history.

3. **Response Generation:**
   - The app checks if the last message was from the user. If so, it proceeds to generate a response.
   - The `get_answer` function (using OpenAI's GPT API) generates a text response based on the conversation history.
   - The `text_to_speech` function (using OpenAI's text-to-speech API) converts the text response into an audio file.
   - The audio file is played automatically, and the text response is displayed in the chat.
   - The assistant's response is added to the conversation history.

4. **Display:**
   - The `st.chat_message` component is used to display the conversation history in a chat-like format, with different styling for user and assistant messages.

5. **Cleanup:**
   - Temporary audio files are deleted.

**Key Function Calls:**

- `speech_to_text(audio_data)`: Converts audio data to text.
- `get_answer(messages)`: Generates a text response based on conversation history.
- `text_to_speech(input_text)`: Converts text to speech.
- `autoplay_audio(file_path)`: Plays an audio file.

This README provides a clear overview of the chatbot's functionality, installation instructions, and a concise explanation of the code's execution flow.
