import streamlit as st
import io
import pandas as pd

def main():
    st.title('La bottega del gusto')

st.markdown(
""""
<style>
body {
    backround-color: #000000;
    color: #FFFFFF;                           /* Imposta il colore del testo a bianco */ }
}
.stApp{ 
    backround-color: #000000;
}
</style>
""",
unsafe_allow_html=True, )


st.title("La mia app con sfondo nero e testo bianco")
st.write("Questo testo bianco è visualizzato su uno sfondo nero.")



if __name__== "__main__":
    main()