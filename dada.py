# Streamlit Timeline Component Example
import streamlit as st
from streamlit_timeline import timeline


html_string = """
            <audio controls autoplay>
              <source src="https://dc585.4shared.com/img/003XNtJ1gm/28cbd634/dlink__2Fdownload_2F003XNtJ1gm_2F_5F-1.mp3_3Fsbsr_3D2967a778cc4983026683ee810d2ae1bfb10_26bip_3DMTgwLjEyOS43My4xMzk_26lgfp_3D52_26bip_3DMTgwLjEyOS43My4xMzk/preview.mp3" type="audio/mp3">
            </audio>
            """
sound = st.empty()
sound.markdown(html_string, unsafe_allow_html=True)

# use full page width
st.set_page_config(page_title="Timeline Example", layout="wide")

# load data
with open('example.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=800)

