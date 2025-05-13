import streamlit as st
import io
import pandas as pd


st.markdown(
    """
    <style>
    .stApp { background-color: #000000; }
    h1 { 
        color: #FFFFFF;  /* Bianco puro */
        text-align: center; 
        font-weight: bold;  /* Testo più spesso */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("La bottega del gusto")

