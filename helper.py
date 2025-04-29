import streamlit as st
import pandas as pd


# for see upload_file
def analyze_csv_file(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df = st.session_state.get('df', df) # for stoping auto refress streamlit
        st.write(df)
