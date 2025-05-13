import streamlit as st
import io
import pandas as pd

st.markdown(
    """
    <style>
    .stApp { background-color: #000000; text-align: center; }
    h1 { color: #FFFFFF; font-weight: bold; }
    .center-container { 
        display: flex; 
        justify-content: center; 
        align-items: center; 
        height: 70vh;  /* Centra verticalmente */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titolo in alto
st.title("La bottega del gusto")

# Contenitore per centrare il bottone
st.markdown('<div class="center-container">', unsafe_allow_html=True)
if st.button("Prenota il tuo tavolo"):
    st.write("🔔 Grazie per la prenotazione! Ti contatteremo a breve.")
st.markdown('</div>', unsafe_allow_html=True)