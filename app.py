import streamlit as st
import io
import pandas as pd

def main():
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


# Bottone interattivo
if st.button("Prenota il tuo tavolo"):
    st.write("🔔 Grazie per la prenotazione! Ti contatteremo a breve.")

if __name__ == "__main__":
    main()