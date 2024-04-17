import streamlit as st
from streamlit_timeline import timeline

# Set page configuration
st.set_page_config(page_title="Anniversary", layout="wide")

# Initialize session state
if 'image_clicked' not in st.session_state:
    st.session_state['image_clicked'] = False

# Function to handle image click
def image_click():
    st.session_state['image_clicked'] = True

# Display the cover image if it hasn't been clicked
if not st.session_state['image_clicked']:
    st.image("https://github.com/hug0sama/hehe/blob/main/IMG_5984.jpeg?raw=true", use_column_width=True, on_click=image_click)

# If the image has been clicked, display the audio player and timeline
if st.session_state['image_clicked']:
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
