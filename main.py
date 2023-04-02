import streamlit as st
import streamlit_survey as ss
import json
import pandas as pd

st.set_page_config(layout="wide")

# Hide streamlit default menu and footer from the template
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden}
    footer {visibility: hidden}
    header {visibility: hidden}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title('Tanvir')

survey = ss.StreamlitSurvey()

pages = survey.pages(3, on_submit=lambda: st.success("Your responses have been recorded. Thank you!"))

##############
with pages:
    if pages.current == 0:
        st.write("Do you have any car?")
        used_before = survey.radio(
            "used_st_before",
            options=["NA","Yes", "No"],
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )

        if used_before == "Yes":
            st.write("Pick you fevorit brand")
            survey.radio(
                "Select One: ", options = ["ALFA", "ROMEO", "ASTON", "MARTIN", "AUDI", "BMW"], horizontal=True, id="1"
                )
            survey.radio(
                "Select One: ", options = ["CHEVROLET","DODGE","FERRARI","HONDA"], horizontal=True, id="2"
                )
            survey.radio(
                "Select One: ", options = ["JAGUAR","LAMBORGHINI","MAZDA","MCLAREN"], horizontal=True, id="3"
                )
            survey.radio(
                "Select One: ", options = ["MERCEDES-BENZ","NISSAN","PAGANI AUTOMOBILI S.P.A","PORSCHE"], horizontal=True, id="4"
                )
            survey.radio(
                "Select One: ", options = ["FIAT","MINI","SCION","SUBARU"], horizontal=True, id="5"
                )
            survey.radio(
                "Select One: ", options = ["BENTLEY","BUICK","FORD","HYUNDAI"], horizontal=True, id="6"
                )
            survey.radio(
                "Select One: ", options = ["LEXUS","MASERATI","ROUSH","VOLKSWAGEN"], horizontal=True, id="7"
                )
            survey.radio(
                "Select One: ", options = ["ACURA","CADILLAC","INFINITI","KIA"], horizontal=True, id="8"
                )
            survey.radio(
                "Select One: ", options = ["MITSUBISHI" ,"ROLLS-ROYCE","TOYOTA","VOLVO"], horizontal=True, id="9"
                )
            survey.radio(
                "Select One: ", options = ["CHRYSLER","LINCOLN","GMC","RAM"], horizontal=True, id="10"
                )
        
        if used_before == "No":
            survey.text_area("How you enjoy this survey", placeholder="Type here")
        
        if used_before == "NA":
            survey.text_area("Write something", placeholder="Type here")
            
#############

json_data = survey.to_json()
st.json(json_data)

df = pd.read_json(json_data)
st.dataframe(df)