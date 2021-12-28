import streamlit as st
from streamlit_player import st_player


url = st.text_input("Second URL", "https://soundcloud.com/imaginedragons/demons")
event = st_player(url)
st.write(event)
