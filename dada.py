import streamlit as st
from streamlit_timeline import timeline

# Set page configuration
st.set_page_config(page_title="Anniversary", layout="wide")

# Initialize session state for audio player visibility
if 'play_audio' not in st.session_state:
    st.session_state['play_audio'] = False

# Function to toggle audio player visibility
def toggle_audio():
    st.session_state['play_audio'] = True

# Center the button in the page
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if not st.session_state['play_audio']:
        # Button to play music
        if st.button('Start Music'):
            toggle_audio()

# If the button has been clicked, display the audio player and timeline
if st.session_state['play_audio']:
    # Audio player
    song_html = """
        <audio controls autoplay>
             <source src="https://github.com/hug0sama/hehe/blob/main/1.mp3?raw=true" type="audio/mp3">
        </audio>
        """
    sound = st.empty()
    sound.markdown(song_html, unsafe_allow_html=True)

    # Load and display timeline
    try:
        with open('example.json', "r") as f:
            data = f.read()
        timeline(data, height=800)
    except Exception as e:
        st.error(f"An error occurred: {e}")
