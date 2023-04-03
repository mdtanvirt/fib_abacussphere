import streamlit as st
import streamlit_survey as ss
import json
import pandas as pd

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages_test = survey.pages(10, on_submit=lambda: st.success("Your responses have been recorded. Thank you Tanvir!"))

with pages_test:
    if pages_test.current == 0:
        st.write("test survey")
        first = survey.radio(
            "Select One: ", options = ["ALFA", "ROMEO", "ASTON", "MARTIN", "AUDI", "BMW"], horizontal=True, id="1"
        )
    if pages_test.current == 1:
        st.write("test survey")
        first = survey.radio(
            "Select One: ", options = ["CHEVROLET","DODGE","FERRARI","HONDA"], horizontal=True, id="2"
        )

    if pages_test.current == 2:
        st.write("test survey")
        first = survey.radio(
            "Select One: ", options = ["JAGUAR","LAMBORGHINI","MAZDA","MCLAREN"], horizontal=True, id="3"
        )

    if pages_test.current == 3:
        st.write("test survey")
        first = survey.radio(
            "Select One: ", options = ["MERCEDES-BENZ","NISSAN","PAGANI AUTOMOBILI S.P.A","PORSCHE"], horizontal=True, id="4"
        )

    if pages_test.current == 4:
        st.write("test survey")
        first = survey.radio(
            "Select One: ", options = ["FIAT","MINI","SCION","SUBARU"], horizontal=True, id="5"
        )

    if pages_test.current == 5:
        st.write("test survey")
        first = survey.radio(
            "Select One: ", options = ["BENTLEY","BUICK","FORD","HYUNDAI"], horizontal=True, id="6"
        )

    if pages_test.current == 6:
        st.write("test survey")
        first = survey.radio(
            "Select One: ", options = ["LEXUS","MASERATI","ROUSH","VOLKSWAGEN"], horizontal=True, id="7"
        )

    if pages_test.current == 7:
        st.write("test survey")
        first = survey.radio(
            "Select One: ", options = ["ACURA","CADILLAC","INFINITI","KIA"], horizontal=True, id="8"
        )

    if pages_test.current == 8:
        st.write("test survey")
        first = survey.radio(
            "Select One: ", options = ["MITSUBISHI","ROLLS-ROYCE","TOYOTA","VOLVO"], horizontal=True, id="9"
        )

    if pages_test.current == 9:
        st.write("test survey")
        first = survey.radio(
            "Select One: ", options = ["CHRYSLER","LINCOLN","GMC","RAM"], horizontal=True, id="10"
        )

json_data = survey.to_json()
st.json(json_data)

df = pd.read_json(json_data)
st.dataframe(df)