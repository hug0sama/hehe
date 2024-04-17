import streamlit as st
from streamlit_timeline import timeline

# Set page configuration
st.set_page_config(page_title="Anniversary", layout="wide")

# Custom CSS to hide the audio controls and make the image cover the full screen
st.markdown("""
    <style>
        .stAudio {
            display: none;
        }
        .cover-image {
            position: fixed;
            top: 0;
            left: 0;
            min-width: 100%;
            min-height: 100%;
            z-index: 9999;
            cursor: pointer;
        }
    </style>
    """, unsafe_allow_html=True)

# Custom JS to hide the image on click and play music
st.markdown("""
    <script>
        function playMusic() {
            var audio = document.getElementById('audio');
            var coverImage = document.getElementById('coverImage');
            coverImage.style.display = 'none';
            audio.play();
        }
    </script>
    """, unsafe_allow_html=True)

# Display the cover image
st.markdown("""
    <img id="coverImage" class="cover-image" src="YOUR_IMAGE_URL" onclick="playMusic()">
    """, unsafe_allow_html=True)

# Audio element
song_html = """
    <audio id="audio">
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
