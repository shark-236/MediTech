import functools
from pathlib import Path

import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.shared import JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd
import plotly.express as px


@st.experimental_memo
def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()
    df.columns = df.columns.str.lower().str.replace(" ", "_", regex=False).str.replace("/", "_", regex=False)

    df = df.fillna("unknown")
    df = df.dropna()

    return df


@st.experimental_memo
def filter_data(
    df: pd.DataFrame, UserID_selections: list(), DoE_selections: list()
) -> pd.DataFrame:

    df = df.copy()
    df = df[
        df.UserID.isin(UserID_selections) & df.loc[df.UserID.isin(UserID_selections), "Date of Entry"].isin(DoE_selections)
    ]

    return df

def main() -> None:
    st.header("Patient Information")

    st.subheader("Upload your CSV")
    uploaded_data = st.file_uploader(
        "Drag and Drop or Click to Upload", type=".csv", accept_multiple_files=False
    )

    if uploaded_data is None:
        st.info("Using example data. Upload a file above to use your own data!")
        uploaded_data = open("dummy.csv", "r")
    else:
        st.success("Uploaded your file!")

    df = pd.read_csv(uploaded_data)
    with st.expander("Raw Dataframe"):
        st.write(df)
    
    df2 = clean_data(df)
    with st.expander("Cleaned Data"):
        st.write(df)

    st.sidebar.subheader("Filter by UserID")

    UserIDs = list(df.UserID.unique())
    UserID_selections = st.sidebar.multiselect(
        "Select UserID to View", options=UserIDs, default=UserIDs
    )
    st.sidebar.subheader("Filter by Date of Entry")

    DoEs = list(df.loc[df.UserID.isin(UserID_selections), "Date of Entry"].unique())
    DoE_selections = st.sidebar.multiselect(
        "Select Dates of Entry to View", options=DoEs, default=DoEs
    )

    df = filter_data(df, UserID_selections, DoE_selections)
    st.subheader("Selected UserIDs and Dates of Entries")


    gb = GridOptionsBuilder.from_dataframe(df)
    
    gb.configure_pagination()
    gb.configure_columns(("UserID", "Date of Entry"), pinned=True)
    gridOptions = gb.build()

    AgGrid(df, gridOptions=gridOptions, allow_unsafe_jscode=True)


if __name__ == "__main__":
    st.set_page_config(
        "Medical Records Viewer by MediTech",
        initial_sidebar_state="expanded",
        layout="wide",
    )
    main()
