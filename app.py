import streamlit as st
import io
import pandas as pd


st.markdown(
    """
    <style>
    .stApp { background-color: #000000; }
    h1 { 
        color: #FFFFFF; 
        text-align: center; 
        font-weight: bold; 
        text-shadow: 2px 2px 5px rgba(255, 255, 255, 0.5);  /* Ombra bianca per contrasto */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("La bottega del gusto")

