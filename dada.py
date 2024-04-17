import streamlit as st
from streamlit_timeline import timeline

# Set page configuration
st.set_page_config(page_title="Anniversary", layout="wide")

# Initialize session state for image visibility
if 'show_image' not in st.session_state:
    st.session_state['show_image'] = True

# Function to toggle image visibility
def toggle_image():
    st.session_state['show_image'] = not st.session_state['show_image']

# Display the cover image if it should be shown
if st.session_state['show_image']:
    st.image("https://github.com/hug0sama/hehe/blob/main/IMG_5984.jpeg?raw=true", use_column_width=True)
    # Button to hide the image and play music
    if st.button('Start Music'):
        toggle_image()

# If the image is not supposed to be shown, display the audio player and timeline
if not st.session_state['show_image']:
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
