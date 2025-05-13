import streamlit as st
import io
import pandas as pd


st.markdown(
    """
    <style>
    .stApp { background-color: #000000; }
    h1 { color: #FFFFFF; }
    p { display: none; }  /* Nasconde qualsiasi testo normale */
    </style>
    """,
    unsafe_allow_html=True
)
st.title("La bottega del gusto")


