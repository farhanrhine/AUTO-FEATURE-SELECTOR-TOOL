import streamlit as st
import pandas as pd

# 1. read any data

# for see upload_file
def analyze_csv_file(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        df = st.session_state.get('df', df) # for stoping auto refress streamlit
        # st.write(df)

# Aim- 2. remove unneddary columns

        if 'columns_removed' not in st.session_state:
            st.write(f"columns:{list(df.columns)}")# it show what columns i have in my dataset

            # i create a multiselect from Streamlit 
            selected_columns = st.multiselect('select any columns which you want to remove',options=df.columns) # this remove multiple columns at once


            if st.button('remove selected columns'):
                if selected_columns:
                    df = df.drop(columns=selected_columns)
                    st.session_state['df']=df # so session remain same , so dont need to again upload
                    # now the second part of this logic, to stop backtracking
                    st.session_state['columns_removed']= True # this stop backtracking

                    st.success(f"columns removed:{','.join(selected_columns)}")# for get a conformation message in green color

                    st.write('## woah! here is your DATASET after removing unwanted columns:')
                    st.write(df)



