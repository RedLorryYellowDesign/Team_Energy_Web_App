
# ---| ALL IMPORT LIBRARIES |---
# Base Streamlit Libraries
import requests # Allows use of URL imports
import streamlit as st # Allows compatibility with Streamlit
from streamlit_lottie import st_lottie # Allows lottie animation
from PIL import Image # Image manipulation
# Data Science Libraries
import plotly as py

# Page configuraion
st.set_page_config(page_title="Team Energy Le Wagon Project", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")

# fucntion to load lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---| IMPORTING ASSEST |---
# Importing lottie animation
lottie_coding_Data_Science_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_xl3sktpc.json")


# ---| ALL FUNCTIONS |---
# Header section
with st.container():
    st.title("Streamlit App")
    st.subheader("This is a Test web app for LeWagon Team Energy")
    st.write("This is a test app for LeWagon Team Energy to test Streamlit")
    st.write("[Le Wagon Home Page](https://www.lewagon.com)")

# ---| USER INPUTS|---

# ---| CALLING API |---

with st.container():
    st.write("---")
    st_lottie(lottie_coding_Data_Science_Animation, height=600)

# ---| DATA VISUALISATION |---

# ---| FOOTER |---


# ---| END OF CODE |---
