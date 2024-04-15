# Streamlit Timeline Component Example
import streamlit as st
from streamlit_timeline import timeline


# use full page width
st.set_page_config(page_title="Timeline Example", layout="wide")

# load data
with open('example.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=800)

import streamlit as st
import time

html_string = """
            <audio controls autoplay>
              <source src="https://soundcloud.com/user-805435019-538938222/ost?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing" type="audio/mp3">
            </audio>
            """

sound = st.empty()
sound.markdown(html_string, unsafe_allow_html=True)  # will display a st.audio with the sound you specified in the "src" of the html_string and autoplay it
