import streamlit as st
import streamlit_survey as ss
import json
import pandas as pd

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")

pages_test = survey.pages(11, on_submit=lambda: st.success("Your responses have been recorded. Thank you Tanvir!"))

with pages_test:
    if pages_test.current == 0:
        st.write("Survey Section-1")
        first = survey.radio(
            "Select One: ", options = ["ALFA", "ROMEO", "ASTON", "MARTIN", "AUDI", "BMW"], horizontal=True, id="1"
        )
    if pages_test.current == 1:
        st.write("Survey Section-2")
        first = survey.radio(
            "Select One: ", options = ["CHEVROLET","DODGE","FERRARI","HONDA"], horizontal=True, id="2"
        )

    if pages_test.current == 2:
        st.write("Survey Section-3")
        first = survey.radio(
            "Select One: ", options = ["JAGUAR","LAMBORGHINI","MAZDA","MCLAREN"], horizontal=True, id="3"
        )

    if pages_test.current == 3:
        st.write("Survey Section-4")
        first = survey.radio(
            "Select One: ", options = ["MERCEDES-BENZ","NISSAN","PAGANI AUTOMOBILI S.P.A","PORSCHE"], horizontal=True, id="4"
        )

    if pages_test.current == 4:
        st.write("Survey Section-5")
        first = survey.radio(
            "Select One: ", options = ["FIAT","MINI","SCION","SUBARU"], horizontal=True, id="5"
        )

    if pages_test.current == 5:
        st.write("Survey Section-6")
        first = survey.radio(
            "Select One: ", options = ["BENTLEY","BUICK","FORD","HYUNDAI"], horizontal=True, id="6"
        )

    if pages_test.current == 6:
        st.write("Survey Section-7")
        first = survey.radio(
            "Select One: ", options = ["LEXUS","MASERATI","ROUSH","VOLKSWAGEN"], horizontal=True, id="7"
        )

    if pages_test.current == 7:
        st.write("Survey Section-8")
        first = survey.radio(
            "Select One: ", options = ["ACURA","CADILLAC","INFINITI","KIA"], horizontal=True, id="8"
        )

    if pages_test.current == 8:
        st.write("Survey Section-9")
        first = survey.radio(
            "Select One: ", options = ["MITSUBISHI","ROLLS-ROYCE","TOYOTA","VOLVO"], horizontal=True, id="9"
        )

    if pages_test.current == 9:
        st.write("Survey Section-10")
        first = survey.radio(
            "Select One: ", options = ["CHRYSLER","LINCOLN","GMC","RAM"], horizontal=True, id="10"
        )

    if pages_test.current == 10:
        st.write("Survey Summary")
        json_data = survey.to_json()
        #st.json(json_data)
        df = pd.read_json(json_data)
        st.dataframe(df)

        # Convert to csv for download button
        @st.cache_data
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)   

        st.download_button(
            label="Download as CSV",
            data=csv,
            file_name='raw.csv',
            mime='text/csv',
        )
        