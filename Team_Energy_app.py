# ---| TEAM ENERGY STREAMLIT WEB APP |--->>>>
# >>>> Site Structure & Desing
# |--------| ------------------------------------------ |
# |SIDE BAR| Page Title                                 |
# |--------| Page Into Text                             |
# |--------| My Pic | MY Work Experience | My Education |
# |--------| ------------------------------------------ |
# |--------| My Skills | My Interests | My Contact Info |
# |--------| ------------------------------------------ |
# |--------| Footer                                     |
# |--------| ------------------------------------------ |
# ---| ALL IMPORT LIBRARIES |--->>>>
# ---| BASE STREAMLIT LIBRARIES |--->>>>
from decimal import FloatOperation
from multiprocessing.sharedctypes import Value
from pickle import FALSE
import requests # Allows use of URL imports
import streamlit as st # Allows compatibility with Streamlit
from streamlit_lottie import st_lottie # Allows lottie animation
from PIL import Image # Image manipulation
# ---| DATASCIANCE LIBRARIES |--->>>>
import plotly as py
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import plotly.figure_factory as ff
import time
# ---| VERIABLES |--->>>>
API_MODE = False
Show_Graph = False
Lottie_off = False
# ---| API ON/OFF DEPENDENT LIBRARIES |--->>>>
if API_MODE == False:
    from Team_Energy.predict  import *
    from Team_Energy.data import create_data, get_weather
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
if Lottie_off == False:
    lottie_coding_Data_Science_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_xl3sktpc.json")
    Team_Lottie_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_vctzcozn.json")
    Loding_Animation = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_ibxFWH.json")
# ---| IMPORTING IMAGES |--->>>>
# ---| SIDE BAR |--->>>>
with st.sidebar:
    st.title("Streamlit App")

# lineplot = st.sidebar.selectbox("Select Plot Type", ["Line Plot", "Bar Plot", "Line Plot with Plotly"])
# ---| Questions |--->>>>
Q1dict = {
  ""'Detached house' : 4,
  "Flat or Maisonette": 0,
  "Semi-detached house": 2,
  "Terraced house": 0
}
Q2dict = {""'Owned outright': 3,
          'Mortgaged': 2,
          'Shared/Equity Ownerhsip': 1,
          'Privately Rented': 0,
          'Social renting': 0
          }

Q3dict = {""'1 bedroom': 0,
          '2 bedrooms': 1,
          '3 bedrooms': 2,
          '4+ bedrooms': 4}

Q4dict = {""'£0-£20,000':0,
          '£20,000-£40,000': 1,
          '£40,000-£60,000': 1,
          '£80,000 +': 4}

def questions(Q1, Q2, Q3, Q4):
    total_values = Q1dict[Q1] + Q2dict[Q2] + Q3dict[Q3] + Q4dict[Q4]
    if total_values > 10:
        User_Group_Selected = 'A'
    elif total_values in range(5,9):
        User_Group_Selected = 'H'
    elif total_values < 5:
        User_Group_Selected = 'Q'
    return User_Group_Selected


# ---| HEADER SECTION |--->>>>
with st.container():
    Header_col_1, Header_col_2, Header_col_3, Header_col_4 = st.columns(4)
    with Header_col_1:
        st.title("Energy.app")
    with Header_col_2:
        st.empty()
    with Header_col_3:
        st.empty()
    with Header_col_4:
        st.empty()
# ---| MAIN SECTION |--->>>>  Cleaned
with st.container():
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["First Question", "Second Question","Qest 3","Qest 4","Qest 5","Qest 6","Qest 7","Submit"])
    with tab1:
        st.write("Please Select your Tarrif Type")
        User_Tarrif_Selected = st.selectbox('Pick one', ["","Fixed Tarrif", "Variable Tarrif"])
        if User_Tarrif_Selected != " ":
            st.warning("Please select a tarrif")
        else:
            User_Tarrif = User_Tarrif_Selected
            st.write (f"You have selected {User_Tarrif} Tarrif")
        with tab2:
            st.write("Please Select your Group Type")
            User_Group_Selected = st.selectbox('Pick one', [" ","A","E","Q"])
    with tab3:
        st.empty()


        # with tab2:
        #     st.write("Please Select your Group Type")
        #     User_Group_Selected = st.selectbox('Pick one', [" ","A","E","Q"])

        with tab3:
            st.write("What is your house type?")
            Question_1 = st.selectbox('Pick one', ['Detached house', "Flat or Maisonette", "Semi-detached house","Terraced house"], key="Question_1")
            if Question_1 != " ":
                st.write("Please select an option")

        with tab4:
            st.write("What is your property ownership status?")
            Question_2 = st.selectbox('Pick one', ['Owned outright', 'Mortgaged', 'Shared/Equity Ownerhsip','Privately Rented', 'Social renting'], key="Question_2")
            if Question_2 != " ":
                st.write("Please select an option")
        with tab5:
            st.write("How many Bedrooms does your house have?")
            Question_3 = st.selectbox('Pick one', ['1 bedroom', '2 bedrooms', '3 bedrooms', '4+ bedrooms'], key="Question_3")
            if Question_3 != " ":
                st.write("Please select an option")
        with tab6:
            st.write("What is your estimated household income?")
            Question_4 = st.selectbox('Pick one', ['£0-£20,000', '£20,000-£40,000','£40,000-£60,000','£80,000 +'], key="Question_4")

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

                with st.spinner('Calling the model'):
                    time.sleep(5)
                st.success('Good so far')

            if User_Tarrif_Selected != '' and User_Group_Selected != '':
                st.write("Model will be called here")
                User_Group_Selected = questions(Q1 = Question_1, Q2 = Question_2, Q3 = Question_3, Q4 = Question_4)

                name = User_Group_Selected
                tariff = User_Tarrif
                # ---| IMPORT JOBLIT MODEL |--->>>>
                filename = f'Team_Energy/model_{name}_{tariff}.joblib'
                m = joblib.load(filename)
                with st.spinner('Spinning up the Hard Drives'):
                    time.sleep(5)
                st.success('All Working Well')
                # ---| PREDICTING |--->>>>
                m = joblib.load(filename)
                with st.spinner('Last Part! This can take a second or two'):
                    time.sleep(5)
                train_df, test_df = create_data(name = name, tariff = tariff)
                train_wd, test_wd = get_weather(train_df, test_df)
                forecast = forecast_model(m,train_wd,test_wd,add_weather=True)
                Show_Graph = True
                st.success('Done, Plostting Graphis now.')


    # with Main_col_2:
        # ---| PLOTTING |--->>>>
        # while Show_Lode == True:
        #     st_lottie(Loding_Animation, speed=1, height=200, key="Loding_Animation")

    #     # ---| PLOTTING |--->>>>
    #     while Show_Lode == True:
    #         st_lottie(Loding_Animation, speed=1, key="v")

#     with Main_col_2:
#         if Show_Graph == True:
#             fig_1 = plt.figure(figsize=(15, 6))
#             sns.lineplot(x=forecast['ds'],y=forecast['yhat'],label='Forecast');
#             sns.lineplot(x=test_df['DateTime'],y=test_df['KWH/hh'],label='Actual');
#             fig_2 = figure(figsize=(15,6))
#             sns.lineplot(x=test_wd['DateTime'],y=test_wd['temperature'],label='Weather');
#             st.pyplot(fig_1)
#             st.pyplot(fig_2)

# with st.container():
#     Main_col_1, Main_col_2 = st.columns((2,4))
#     with Main_col_1:
#         # Insert containers separated into tabs:
#         tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["First Question", "Second Question", "Third Question", "Fourth Question", "Fifth Question", "Sixth Question", "Seventh Question"])
#         with tab1:
#             st.write("Please Select your Tarrif Type")
#             User_Tarrif_Selected = st.selectbox('Pick one', ["","Fixed Tarrif", "Variable Tarrif"])
#             if User_Tarrif_Selected == "Fixed Tarrif":
#                 User_Tarrif = "Std"
#                 st.write("You have selected Fixed Tarrif")
#             elif User_Tarrif_Selected == "Variable Tarrif":
#                 User_Tarrif = "ToU"
#                 st.write("You have selected Variable Tarrif")
#             else:
#                 st.write("Please select a tarrif")

with st.container():
    if Show_Graph == True:
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
        fig_1 = plt.figure(figsize=(15, 6))
        sns.lineplot(x=forecast['ds'],y=forecast['yhat'],label='Forecast');
        sns.lineplot(x=test_df['DateTime'],y=test_df['KWH/hh'],label='Actual');
        fig_2 = figure(figsize=(15,6))
        sns.lineplot(x=test_wd['DateTime'],y=test_wd['temperature'],label='Weather');
        with st.spinner('Wait for it...'):
            time.sleep(5)
        st.success('Done!')
        st.pyplot(fig_1)
        st.pyplot(fig_2)
# ---| MAIN SECTION |--->>>>

# with st.container():
#     st.write("---")
#     Main_col_1, Main_col_2 = st.columns((2,4))
#     with Main_col_1:
#         # Insert containers separated into tabs:
#         tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["First Question", "Second Question", "Third Question", "Fourth Question", "Fifth Question", "Sixth Question", "Seventh Question"])
#         with tab1:
#             st.write("Please Select your Tarrif Type")
#             User_Tarrif_Selected = st.selectbox('Pick one', ["","Fixed Tarrif", "Variable Tarrif"])
#             if User_Tarrif_Selected == "Fixed Tarrif":
#                 User_Tarrif = "Std"
#                 st.write("You have selected Fixed Tarrif")
#             elif User_Tarrif_Selected == "Variable Tarrif":
#                 User_Tarrif = "ToU"
#                 st.write("You have selected Variable Tarrif")
#             else:
#                 st.write("Please select a tarrif")

#         with tab2:
#             st.write("Please Select your Group Type")
#             User_Group_Selected = st.selectbox('Pick one', [" ","A","E","Q"])

#         with tab3:
#             st.write("Question 1 Text")
#             Question_1 = st.selectbox('Pick one', [" ","A","E","Q"], key="Question_1")
#             if Question_1 != " ":
#                 st.write("Please select an option")
# --------------------------------------------------------------------------------
            # st_fig.update_layout(
            #     title='Line Plot',
            #     xaxis_title='X axis',
            #     yaxis_title='Y axis'
            #     )
            # #st_fig.show()
            # st.plotly_chart(st_fig, use_container_width= True)
# --------------------------------------------------------------------------------
#         with tab4:
#             st.write("Question 1 Text")
#             Question_2 = st.selectbox('Pick one', [" ","A","E","Q"], key="Question_2")
#             if Question_2 != " ":
#                 st.write("Please select an option")
#         with tab5:
#             st.write("Question 1 Text")
#             Question_3 = st.selectbox('Pick one', [" ","A","E","Q"], key="Question_3")
#             if Question_3 != " ":
#                 st.write("Please select an option")
#         with tab6:
#             st.write("Question 1 Text")
#             Question_4 = st.selectbox('Pick one', [" ","A","E","Q"], key="Question_4")

#             if Question_4 != " ":
#                 st.write("Please select an option")
#         with tab7:
#             st.write("Question 1 Text")
#             Question_5 = st.selectbox('Pick one', [" ","A","E","Q"], key="Question_5")
#             if Question_5 != " ":
#                 st.write("Please select an option")
        # Submit Button
    #     if st.button("Submit"):
    #         # Predict_Model(User_Tarrif_Selected,User_Group_Selected )
    #         if User_Tarrif_Selected != "" and User_Group_Selected != " ":
    #             with st.spinner('Calling the model'):
    #                 time.sleep(5)
    #             st.success('Good so far')
    #             name = User_Group_Selected
    #             tariff = User_Tarrif
    #             # ---| IMPORT JOBLIT MODEL |--->>>>
    #             filename = f'Team_Energy/model_{name}_{tariff}.joblib'
    #             m = joblib.load(filename)
    #             with st.spinner('Spinning up the Hard Drives'):
    #                 time.sleep(5)
    #             st.success('All Working Well')
    #             # ---| PREDICTING |--->>>>
    #             m = joblib.load(filename)
    #             with st.spinner('Last Part! This can take a second or two'):
    #                 time.sleep(5)
    #             train_df, test_df = create_data(name = name, tariff = tariff)
    #             train_wd, test_wd = get_weather(train_df, test_df)
    #             forecast = forecast_model(m,train_wd,test_wd,add_weather=True)
    #             Show_Graph = True
    #             st.success('Done, Plostting Graphis now.')

    # with Main_col_2:
    #     if Show_Graph == True:
    #         my_bar = st.progress(0)
    #         for percent_complete in range(100):
    #             time.sleep(0.1)
    #         my_bar.progress(percent_complete + 1)
    #         fig_1 = plt.figure(figsize=(15, 6))
    #         sns.lineplot(x=forecast['ds'],y=forecast['yhat'],label='Forecast');
    #         sns.lineplot(x=test_df['DateTime'],y=test_df['KWH/hh'],label='Actual');
    #         fig_2 = figure(figsize=(15,6))
    #         sns.lineplot(x=test_wd['DateTime'],y=test_wd['temperature'],label='Weather');
    #         with st.spinner('Wait for it...'):
    #             time.sleep(5)
    #         st.success('Done!')
    #         st.pyplot(fig_1)
    #         st.pyplot(fig_2)
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
