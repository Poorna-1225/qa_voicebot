import streamlit as st
import os
from utils import get_answer, text_to_speech, autoplay_audio, speech_to_text
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *

# Float feature initialization
float_init()

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! How may I assist you today?"}
        ]
    # if "audio_initialized" not in st.session_state:
    #     st.session_state.audio_initialized = False

initialize_session_state()

st.title("OpenAI Conversational Chatbot 🤖")

# Create footer container for the microphone
footer_container = st.container()
with footer_container:
    audio_bytes = audio_recorder() # audio_bytes is having all the speech we record using recorder.


for message in st.session_state.messages:
    with st.chat_message(message["role"]): #st.chat_message creates a text field where we can write the text messages.
        st.write(message["content"])  # st.write is used to write the text in the texfield we created. 

if audio_bytes:
    # Write the audio bytes to a file
    with st.spinner("Transcribing..."): #st.spinner displays the spinner with given text next to it.
        webm_file_path = "temp_audio.mp3" # webm_file_path = the string we defined.
        with open(webm_file_path, "wb") as f:
            f.write(audio_bytes) # we are opening that file(temp_audio.mp3 which is stored in webm_file_path) and writing all the audio recorded.
            #technically now temp_auido.mp3 stores audio recorded every single time.

        transcript = speech_to_text(webm_file_path) # we are calling stt function and passing the webm_file_path as parameter which is having the auido recorded in it and this function returns the text as ouptput. it converts the audio recorded into text.
        if transcript: # if it is having text then we append that to the session_state.messages and then remove the file_path since it can store the next message.
            st.session_state.messages.append({"role": "user", "content": transcript})
            with st.chat_message("user"):
                st.write(transcript)
            os.remove(webm_file_path)

if st.session_state.messages[-1]["role"] != "assistant":
    # it checks if the last message in the history is from the user.
    # if it is from user, then it created a text field saying assistant and folled by spinner saying thinking
    # then it calls the get_answer function from the utils.py file and pass the session_state.messages to get the answer.
    # then generate the audio response by passing the text response as input.
    # finally play the auido using the function auto_play 
    with st.chat_message("assistant"):
        with st.spinner("Thinking🤔..."):
            final_response = get_answer(st.session_state.messages)
        with st.spinner("Generating audio response..."):    
            audio_file = text_to_speech(final_response)
            autoplay_audio(audio_file)
        st.write(final_response)
        st.session_state.messages.append({"role": "assistant", "content": final_response})
        os.remove(audio_file)

# Float the footer container and provide CSS to target it with
footer_container.float("bottom: 0rem;")