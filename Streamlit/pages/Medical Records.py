import functools
from pathlib import Path

import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.shared import JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd
import plotly.express as px
from datetime import datetime as dt


@st.experimental_memo
def clean_data(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()
    df = df.rename({'Date of Entry':'Date'}, axis = 1)
    df.iloc[:,0] = pd.to_datetime(df.iloc[:,0])

    df = df.fillna("unknown")
    df = df.dropna()

    return df


@st.experimental_memo
def filter_data(
    df: pd.DataFrame, UserID_selections: list(), DoE_selections: list()
) -> pd.DataFrame:
    df = df.copy()
    df = df[
        df.UserID.isin(UserID_selections) & df.Date.isin(DoE_selections.iloc[:,0])
    ]
    
    return df

def main() -> None:
    st.header("Patient Information Viewer")

    st.subheader("Upload your CSV")
    uploaded_data = st.file_uploader(
        "Drag and Drop or Click to Upload", type=".csv", accept_multiple_files=False
    )

    if uploaded_data is None:
        st.info("Using example data. Upload a file above to use your own data!")
        uploaded_data = open("dummyhipaa.csv", "r")
    else:
        st.success("Uploaded your file!")

    df = pd.read_csv(uploaded_data)
    with st.expander("Raw Dataframe"):
        st.write(df)
    
    df = clean_data(df)
    with st.expander("Cleaned Data"):
        st.write(df)

    st.sidebar.subheader("Filter by UserID")

    UserIDs = list(df.UserID.unique())
    UserID_selections = st.sidebar.multiselect(
        "Select UserID to View", options=UserIDs, default=UserIDs
    )
    
    st.sidebar.subheader("Filter by Date of Entry")
    dts = st.sidebar.date_input(label='Date Range: ',
                value=(dt(day=20, month=12, year=2022), 
                        dt(day=30, month=12, year=2022)),
                key='#date_range',
                help="The start and end date time")
    st.sidebar.write('Start: ', dts[0], "End: ", dts[1])
    
    daterange = pd.date_range(start = dts[0], end =dts[1]).to_frame(index=False) #making date range dataframe for filter
    
    df1 = filter_data(df, UserID_selections, daterange)
    st.subheader("Selected UserIDs and Dates of Entries")

    gb = GridOptionsBuilder.from_dataframe(df1)
    
    gb.configure_pagination()
    gb.configure_columns(("UserID", "Date"), pinned=True)
    gridOptions = gb.build()

    AgGrid(df1, gridOptions=gridOptions, allow_unsafe_jscode=True)


if __name__ == "__main__":
    st.set_page_config(
        "Medical Records Viewer by MediTech",
        initial_sidebar_state="expanded",
        layout="wide",
    )
    main()
