import streamlit as st
from ddl import create_n_insert

create_n_insert()

st.set_page_config(layout='wide')

st.sidebar.title('Adventure Works')

customers_page = st.Page(
    'pages/customers.py',
    title='Customers',
    default=True
)

pgs = st.navigation([customers_page])
pgs.run()