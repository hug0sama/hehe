import streamlit as st
from streamlit_timeline import timeline

st.set_page_config(page_title="Anniversary", layout="wide")


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
