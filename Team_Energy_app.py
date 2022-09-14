# ---| ALL IMPORT LIBRARIES |--->>>>
# ---| BASE STREAMLIT LIBRARIES |--->>>>
from decimal import FloatOperation
from pickle import FALSE
import requests # Allows use of URL imports
import streamlit as st # Allows compatibility with Streamlit
from streamlit_lottie import st_lottie # Allows lottie animation
from PIL import Image # Image manipulation
# ---| DATASCIANCE LIBRARIES |--->>>>
import plotly as py
import plotly.express as px
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import plotly.figure_factory as ff

# ---| API ON/OFF DEPENDENT LIBRARIES |--->>>>
API_MODE = False
if API_MODE == False:
    from Team_Energy.predict  import *
    from Team_Energy.data import create_data, get_weather
# ---| VERIABLES |--->>>>
Show_Graph = False
# ---| PAGE CONFIGURATION |--->>>>
st.set_page_config(page_title="Team Energy Le Wagon Project", page_icon=":zap:", layout="wide", initial_sidebar_state="expanded")
# ---| LOAD CSS FOR STYLEING |---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style/style.css")
# ---| LOTTIE ANIMATION FUNCTIONS |--->>>>
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
# ---| CALL API FROM GCP |--->>>>
def API_REQUESTS(url):
    if API_MODE == True:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    else:
        st.write("API Call is set to False, Please Enable API Call")
# ---| POST API |--->>>>
def API_POST(url, data):
    if API_MODE == True:
        r = requests.post(url, data=data)
        if r.status_code != 200:
            return None
        return r.json()
    else:
        st.write("API Call is set to False, Please Enable API Call")
# ---| CALLING PREDICT MODEL |--->>>>
def Predict_Model(User_Tarrif_Selected,User_Group_Selected ):
    if User_Tarrif_Selected != "" and User_Group_Selected != " ":
            st.write("Model will be called here")
            name = User_Group_Selected
            tariff = User_Tarrif
            # ---| IMPORT JOBLIT MODEL |--->>>>
            filename = f'Team_Energy/model_{name}_{tariff}.joblib'
            m = joblib.load(filename)
            st.write("model loaded succcessfully")
            # ---| PREDICTING |--->>>>
            train_df, test_df = create_data(name = name, tariff = tariff)
            train_wd, test_wd = get_weather(train_df, test_df)
            forecast = forecast_model(m,train_wd,test_wd,add_weather=True)
    else :
        st.write("Please Select both a Tarrif and Group")
# ---| SEABORN PLOT FUNCTIONS |--->>>>
def seabon_line_plot(x, y, title, xlabel, ylabel, hue=None):
    fig_01, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=x, y=y, hue=hue)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig_01)
# ------>>>>
def seabon_bar_plot(df, x, y, title, xlabel, ylabel, hue=None):
    fig_02, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x=x, y=y, hue=hue)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    st.pyplot(fig_02)
# ---| PLOTLY PLOT FUNCTIONS |--->>>>
def plotly_line_plot(df, x, y, title, xlabel, ylabel, hue=None):
    fig_03 = py.line(df, x=x, y=y, title=title, labels={x:xlabel, y:ylabel}, color=hue)
    st.plotly_chart(fig_03)
# ---| IMPORTING LOTTIE ASSEST |---
lottie_coding_Data_Science_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_xl3sktpc.json")
Team_Lottie_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_vctzcozn.json")
# ---| IMPORTING IMAGES |--->>>>

# ---| SIDE BAR |--->>>>
# lineplot = st.sidebar.selectbox("Select Plot Type", ["Line Plot", "Bar Plot", "Line Plot with Plotly"])
# ---| HEADER SECTION |--->>>>
with st.container():
    Header_col_1, Header_col_2, Header_col_3, Header_col_4 = st.columns(4)
    with Header_col_1:
        st.title("Streamlit App")
        st.subheader("This is a Test web app for LeWagon Team Energy")
        st.write("This is a test app for LeWagon Team Energy to test Streamlit")
        st.write("[Le Wagon Home Page](https://www.lewagon.com)")
    with Header_col_2:
        st.empty()
    with Header_col_3:
        st.empty()
    with Header_col_4:
        st.empty()
# ---| MAIN SECTION |--->>>>
with st.container():
    Main_col_1, Main_col_2 = st.columns((2,4))
    with Main_col_1:
        # Insert containers separated into tabs:
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["First Question", "Second Question", "Third Question", "Fourth Question", "Fifth Question", "Sixth Question", "Seventh Question"])
        with tab1:
            st.write("Please Select your Tarrif Type")
            User_Tarrif_Selected = st.selectbox('Pick one', ["","Fixed Tarrif", "Variable Tarrif"])
            if User_Tarrif_Selected == "Fixed Tarrif":
                User_Tarrif = "Std"
                st.write("You have selected Fixed Tarrif")
            elif User_Tarrif_Selected == "Variable Tarrif":
                User_Tarrif = "ToU"
                st.write("You have selected Variable Tarrif")
            else:
                st.write("Please select a tarrif")

        with tab2:
            st.write("Please Select your Group Type")
            User_Group_Selected = st.selectbox('Pick one', [" ","A","E","Q"])

        with tab3:
            st.write("Question 1 Text")
            Question_1 = st.selectbox('Pick one', [" ","A","E","Q"], key="Question_1")
            if Question_1 != " ":
                st.write("Please select an option")

        with tab4:
            st.write("Question 1 Text")
            Question_2 = st.selectbox('Pick one', [" ","A","E","Q"], key="Question_2")
            if Question_2 != " ":
                st.write("Please select an option")
        with tab5:
            st.write("Question 1 Text")
            Question_3 = st.selectbox('Pick one', [" ","A","E","Q"], key="Question_3")
            if Question_3 != " ":
                st.write("Please select an option")
        with tab6:
            st.write("Question 1 Text")
            Question_4 = st.selectbox('Pick one', [" ","A","E","Q"], key="Question_4")

            if Question_4 != " ":
                st.write("Please select an option")
        with tab7:
            st.write("Question 1 Text")
            Question_5 = st.selectbox('Pick one', [" ","A","E","Q"], key="Question_5")
            if Question_5 != " ":
                st.write("Please select an option")

        # Submit Button
        if st.button("Submit"):
            # Predict_Model(User_Tarrif_Selected,User_Group_Selected )
            if User_Tarrif_Selected != "" and User_Group_Selected != " ":
                st.write("Model will be called here")
                name = User_Group_Selected
                tariff = User_Tarrif
                # ---| IMPORT JOBLIT MODEL |--->>>>
                filename = f'Team_Energy/model_{name}_{tariff}.joblib'
                m = joblib.load(filename)
                st.write("model loaded succcessfully")
                # ---| PREDICTING |--->>>>
                train_df, test_df = create_data(name = name, tariff = tariff)
                train_wd, test_wd = get_weather(train_df, test_df)
                forecast = forecast_model(m,train_wd,test_wd,add_weather=True)
                Show_Graph = True

    with Main_col_2:
        # ---| PLOTTING |--->>>>
        if Show_Graph == True:
            fig_1 = plt.figure(figsize=(15, 6))
            sns.lineplot(x=forecast['ds'],y=forecast['yhat'],label='Forecast');
            sns.lineplot(x=test_df['DateTime'],y=test_df['KWH/hh'],label='Actual');
            fig_2 = figure(figsize=(15,6))
            sns.lineplot(x=test_wd['DateTime'],y=test_wd['temperature'],label='Weather');
            st.pyplot(fig_1)
            st.pyplot(fig_2)

            fig_43 = px.line(x=forecast['ds'],y=forecast['yhat'],title ='Forecast');


            # # ---| PLOTLY PLOT |--->>>>
            st.plotly_chart(fig_43)

# ---| FOOTER SECTION|--->>>>
with st.container():
    st.write("---")
    Flooter_col_1, Flooter_col_2, Flooter_col_3, Flooter_col_4 = st.columns(4)
    with Flooter_col_1:
        st.subheader("The Team")
        st.write("This app was created by the Team Energy. The Team Energy is a group of 4 students from Le Wagon Data Science Bootcamp. The Team Energy is made up of the following members:")
    with Flooter_col_2:
        st_lottie(Team_Lottie_Animation, speed=1, key="i")
    with Flooter_col_3:
        st.write("Zenan Ahmed")
        st.write("[ZenanAH](https://github.com/ZenanAH)")
        st.write("---")
        st.write("Chris Cockerill")
        st.write("[Ruston3](https://github.com/Ruston3)")
    with Flooter_col_4:
        st.write("Jordan Harris")
        st.write("[RedLorryYellowDesign](https://github.com/RedLorryYellowDesign)")
        st.write("---")
        st.write("Jordan Haynes")
        st.write("[haynesj1](https://github.com/haynesj1)")
# ---| END OF CODE |--->>>>
        # my_slider_val = st.slider('Quinn Mallory', 1, 88)
        # st.text('Fixed width text')
        # st.markdown('_Markdown_') # see *
        # st.latex(r''' e^{i\pi} + 1 = 0 ''')
        # st.write('Most objects') # df, err, func, keras!
        # st.write(['st', 'is <', 3]) # see *
        # st.title('My title')
        # st.header('My header')
        # st.subheader('My sub')
        # st.code('for i in range(8): foo()')
        # st.markdown("This **word** is bold. This <em>word</em> is italic.")
