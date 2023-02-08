import functools
from pathlib import Path

import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.shared import JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import pandas as pd
import plotly.express as px


def main() -> None:
    st.header("Patient Information Logger")

    st.subheader("Upload empty CSV")
    uploaded_data = st.file_uploader(
        "Drag and Drop or Click to Upload", type=".csv", accept_multiple_files=False
    )

    if uploaded_data is None:
        st.info("Using example empty. Upload a file above to use your own data!")
        uploaded_data = open("empty.csv", "r")
    else:
        st.success("Uploaded your file!")

    df = pd.read_csv(uploaded_data)
    with st.expander("Raw Dataframe"):
        st.write(df)

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
