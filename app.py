import streamlit as st
from helper import *

# Aim- 1
def main():
    st.title("AUTO FEATURE SELECTOR TOOL")

    # file uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type='csv')
    # takeing that helper.py define funtion here
    if uploaded_file is not None:
        analyze_csv_file(uploaded_file)


if __name__ == "__main__":
    main()

# Aim -2

