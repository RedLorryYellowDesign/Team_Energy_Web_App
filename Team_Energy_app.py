
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

# ---| MODEL WILL BE CALLE HERE |---
def model_call(User_Tarrif_Selected,User_Group_Selected): # model will be called here
    return 0

# ---| ALL FUNCTIONS |---
# Header section
with st.container():
    st.title("Streamlit App")
    st.subheader("This is a Test web app for LeWagon Team Energy")
    st.write("This is a test app for LeWagon Team Energy to test Streamlit")
    st.write("[Le Wagon Home Page](https://www.lewagon.com)")

# ---| USER INPUTS|---

with st.container():
    Col_1,Col_2,Col_3 = st.columns(3)

    with Col_1:
        # tarrif
        st.subheader("Pease Select your Tarrif Type")
        User_Tarrif_Selected = st.selectbox('Pick one', ["","Fixed Tarrif", "Variable Tarrif"])
        if User_Tarrif_Selected == "Fixed Tarrif":
            User_Tarrif = 1
        elif User_Tarrif_Selected == "Variable Tarrif":\
            User_Tarrif = 0
        else:
            st.write("Please select a tarrif")

        # Group
        st.subheader("Pease Select your Group")
        User_Group_Selected = st.selectbox('Pick one', ["","Group1", "Group2", "Group3"])
        if User_Group_Selected == "Group1":
            User_Group = 1
        elif User_Group_Selected == "Group2":
            User_Group = 2
        elif User_Group_Selected == "Group3":
            User_Group = 3
        else:
            st.write("Please select a Group")

        # Submit Button
        if st.button("Submit"):
            st.write("Model will be called here")
            st.write(model_call(User_Tarrif_Selected,User_Group_Selected))
        else:
            st.write("Opps something went wrong")


        with Col_2:
            st.write("---")
            st_lottie(lottie_coding_Data_Science_Animation, height=600)

        with Col_3:
            st.write("---")
            st.write("---")
            st.write("---")

# ---| DATA VISUALISATION |---

# ---| FOOTER |---

# ---| END OF CODE |---
