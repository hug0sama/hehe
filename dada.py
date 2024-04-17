import streamlit as st
from streamlit_timeline import timeline

st.set_page_config(page_title="Anniversary", layout="wide")

if 'play_audio' not in st.session_state:
    st.session_state['play_audio'] = False
    st.session_state['image_clicked'] = False

# Function to play audio and hide the image
def play_audio():
    if not st.session_state['image_clicked']:  # Check if the image has not been clicked before
        st.session_state['play_audio'] = True
        st.session_state['image_clicked'] = True  # Set to True after the first click

# Display a transparent image that covers the entire page
# Users can click on the image to trigger audio playback
if not st.session_state['image_clicked']:  # Only display the image if it hasn't been clicked
    transparent_image_url = 'path_to_your_transparent_image.png'  # Replace with your transparent image URL
    st.markdown(f'<img src="https://github.com/hug0sama/hehe/blob/main/IMG_5992.png?raw=true" alt="Transparent Image" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 9999;" onclick="play_audio()">', unsafe_allow_html=True)

# Check if audio should be played
if st.session_state['play_audio']:
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
