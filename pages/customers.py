import pandas as pd
import plotly.express as px
import streamlit as st

import db

st.header("Customers demographics")

min_date, max_date = db.fetch_date_boundaries()

with st.sidebar:
    st.write('---')
    st.subheader('Main filters')
    edate = st.date_input(
        label = 'Select report date',
        min_value = min_date,
        max_value = max_date,
        value = max_date
    )
    st.write('---')
    st.subheader('Additional filters')


custs_df = db.fetch_customers(edate)

duration = st.sidebar.number_input(
        'Select the duration of customer experience',
        min_value = custs_df['duration'].min(),
        max_value = custs_df['duration'].max(),
        value = int(custs_df['duration'].mean())
    )

duration_filter = f"duration <= {duration}"
filters = f"{duration_filter}"

custs_filtered = custs_df.query(filters)



col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    'Number of customers',
    custs_filtered['customer_key'].nunique()
)

col2.metric(
    'Average customer age',
    int(custs_filtered['age'].mean())
)

col3.metric(
    'Median customer age',
    int(custs_filtered['age'].median())
)


r2_col1, r2_col2 = st.columns(2)
gender_pie = px.pie(
    data_frame=custs_filtered['gender'].value_counts().to_frame().reset_index(),
    values='count',
    names='gender',
    title='Breakdown by gender'
)

r2_col1.plotly_chart(gender_pie)

marital_df = custs_filtered['marital_status'].value_counts().to_frame().reset_index()

marital_pie = px.pie(
    data_frame=marital_df,
    values='count',
    names='marital_status',
    hole=.5,
    title='Breakdown by marital status',
    color = 'marital_status',
    color_discrete_map={'M': 'lightgreen', 'S': 'lightgray'}
)
r2_col2.plotly_chart(marital_pie)



ages_distribution = px.histogram(
    data_frame=custs_filtered,
    x='age',
    color='gender',
    title='Age distribution'
)

st.plotly_chart(ages_distribution)

st.dataframe(custs_filtered)