import pandas as pd
import plotly.express as px
import streamlit as st

import db

st.header("Customers demographics")

min_date, max_date = db.fetch_date_boundaries()

with st.sidebar:
    edate = st.date_input(
        label = 'Select report date',
        min_value = min_date,
        max_value = max_date,
        value = max_date
    )


custs_df = db.fetch_customers(edate)

st.dataframe(custs_df)