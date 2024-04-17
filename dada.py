import streamlit as st
from streamlit_timeline import timeline

# Set page configuration
st.set_page_config(page_title="Anniversary", layout="wide")

# Callback function to play audio
def play_audio():
    st.session_state['play_audio'] = True

# Initialize session state for audio player visibility
if 'play_audio' not in st.session_state:
    st.session_state['play_audio'] = False

# Center the button in the page
col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    if not st.session_state['play_audio']:
        # Button to play music
        st.button('Start Music', on_click=play_audio)

# If the button has been clicked, play the music without displaying the audio player
if st.session_state['play_audio']:
    # Audio element (hidden)
    song_html = """
        <audio autoplay>
             <source src="https://github.com/hug0sama/hehe/blob/main/1.mp3?raw=true" type="audio/mp3">
        </audio>
        """
    st.markdown(song_html, unsafe_allow_html=True)

    # Load and display timeline
    try:
        with open('example.json', "r") as f:
            data = f.read()
        timeline(data, height=800)
    except Exception as e:
        st.error(f"An error occurred: {e}")
