import functools
from pathlib import Path

import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.shared import JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd
import plotly.express as px
from datetime import datetime as dt

def symptom() -> None:
    form = st.form(key="form_settings1")
    expander2 = form.expander("Symptom Information")
    sym1 = expander2.text_input(
        "Symptom 1",
        max_chars=100,
        key="Symptom1",
    )
    sym2 = expander2.text_input(
        "Symptom 2",
        max_chars=100,
        key="Symptom2",
    )
    sym3 = expander2.text_input(
        "Symptom 3",
        max_chars=100,
        key="Symptom3",
    )
    form.form_submit_button(label="Submit")

def form() -> None:
    form = st.form(key="form_settings")
    col1, col2, col3, col4 = form.columns([2, 1, 1, 1])

    date = col2.date_input(
        "Date of Entry",
        key="Date of Entry",
    )
    UserID = col1.text_input(
        "Patient ID",
        key="UserID",
    )
    Sex = ["M", "F"]
    shape = col4.radio(
        "Patient Sex",
        options=Sex,
        key="Sex",
    )
    consent = col3.selectbox(
        "Patient Consent",
        options=["no","yes"],
        key="consent",
    )

    expander = form.expander("Trial Information")
    col1clinic, col2clinic = expander.columns([1,1])

    clinic = col1clinic.text_input(
        "Clinic Identifier",
        max_chars=10,
        key="ClinicID",
    )
    cliniczip = col1clinic.text_input(
        "Clinic Zipcode",
        max_chars=10,
        key="Clinic ZIP",
    )
    group = col2clinic.text_input(
        "Group",
        max_chars=10,
        key="Group",
    )
    phase = col2clinic.text_input(
        "Phase",
        max_chars=10,
        key="Phase",
    ) 
    
    expander1 = form.expander("Medical Information")
    col1med, col2med = expander1.columns([1,1])

    bp = col1med.text_input(
        "Blood Pressure",
        max_chars=10,
        key="BloodPressure",
    )
    btmp = col1med.text_input(
        "Body Temperature",
        max_chars=10,
        key="BodyTemp",
    )
    fast = col2med.text_input(
        "Fasting?",
        max_chars=10,
        key="Fast",
    )
    medic = col2med.text_input(
        "Medication Administered",
        max_chars=10,
        key="Medic",
    )
    result = expander1.text_input(
        "Result",
        max_chars=100,
        key="Result",
    ) 
    
    Sym = form.radio(
        "Symptoms",
        options=["no","yes"],
        key="sym",
    )
    if Sym == "yes":
        symptom()

    form.form_submit_button(label="Submit")

def main() -> None:
    st.header("Patient Information Logger")

    st.subheader("Empty CSV")

    df = pd.read_csv(open("empty.csv", "r"))
    with st.expander("Raw Dataframe"):
        st.write(df)
    st.subheader("Enter Patient Information")
    
    form()
    
    st.subheader("Entered Information")

    gb = GridOptionsBuilder.from_dataframe(df)
    
    gb.configure_pagination()
    gb.configure_columns(("UserID", "Date of Entry"), pinned=True)
    gridOptions = gb.build()

    AgGrid(df, gridOptions=gridOptions, allow_unsafe_jscode=True)
    
    st.download_button("Download Entry",
                       df.to_csv(),
                       file_name = 'Data Entry',
                       mime = 'text/csv')

if __name__ == "__main__":
    st.set_page_config(
        "Medical Records Logger by MediTech",
        initial_sidebar_state="expanded",
        layout="wide",
    )
    main()
    