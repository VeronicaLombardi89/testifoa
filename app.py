import streamlit as st
import io
import pandas as pd

def main():
    st.title('La bottega del gusto')

# Inserire CSS corretto per lo stile della pagina
st.markdown(
    """
    <style>
    .stApp { 
        background-color: #000000;
        color: #FFFFFF;  /* Testo bianco */
    }
    h1, h2, h3, h4, h5, h6, p, div {
        color: #FFFFFF !important;  /* Assicura che tutto il testo sia bianco */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titolo e contenuto della pagina
st.title("La mia app con sfondo nero e testo bianco")
st.write("Questo testo bianco è visualizzato su uno sfondo nero.")


if __name__== "__main__":
    main()