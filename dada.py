import streamlit as st
from streamlit_timeline import timeline

clicked = false

st.set_page_config(page_title="Anniversary", layout="wide")

st.markdown(f'<img src="https://github.com/hug0sama/hehe/blob/main/IMG_5992.png?raw=true" alt="Transparent Image" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 9999;" onclick="play_audio()">', unsafe_allow_html=True)

# Check if audio should be played
def play_audio():
    html_string = """
            <audio controls autoplay="true">
              <source src="https://github.com/hug0sama/hehe/blob/main/1.mp3?raw=true" type="audio/mp3">
            </audio>
            """
    sound = st.empty()
    sound.markdown(html_string, unsafe_allow_html=True)


with open('example.json', "r") as f:
    data = f.read()
    
timeline(data, height=800)
