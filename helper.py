import streamlit as st
import pandas as pd
from sklearn.impute import SimpleImputer
from fancyimpute import IterativeImputer


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

# Aim- 3. show & handle missing or duplicate data

        missing_value = df.isnull().sum()
        these_has_missing_values = missing_value.sum()> 0

        duplicate_count = df.duplicated().sum()
        these_has_duplicateds_values = duplicate_count > 0

        if these_has_missing_values or these_has_duplicateds_values:
            st.warning(f"These are missing/duplicated values inside your dataset '(in your selected columns)' ",)

            if these_has_missing_values:
                st.write('### Missing values')
                st.write(missing_value[missing_value > 0]) # show missing value in a table pandas i used
# '''there are multiple types of handling missing values so i give some option to handle differnt kind of missing values and fill them '''
# here loop running only column which have a missing value

                # option to handling missing value
                for column in missing_value[missing_value > 0].index: # this handle in a sequence with the help of index so , all missing values columns are handle by sequence .
                    st.write(f"#### column: {column}")


                    # option to remove missing value
                if st.button(f"remove rows with missing value in {column}"):
                    df = df.dropna(subset=[column])
                    st.session_state['df']= df
                    st.success(f" you bro ! All Row with missing values in '{column}' remove successfully.")


                    # fill the missing value with mean

                if st.button(f"fill missing values in {column} with mean "):

                   imputer = SimpleImputer(strategy='mean') 
                   df[column] = imputer.fit_transform(df[[column]])

                   st.session_state['df']=df
                   st.success(f"Missing value in '{column}'filled with mean.") 

                    # fill the missing value with median


                if st.button(f"fill missing values in {column} with median "):

                   imputer = SimpleImputer(strategy='median') 
                   df[column] = imputer.fit_transform(df[[column]])

                   st.session_state['df']=df
                   st.success(f"Missing value in '{column}'filled with median.")


                   # missing value with mode

                if st.button(f"fill missing value in '{column}' filled with mode."):

                    mode_value = df[column].mode()[0]
                    df[column].fillna(mode_value,inplace=True)

                    st.session_state['df']= df
                    st.success(f"Missing values in '{column}' filled with mode. ")

                    # fill custom value
                    custom_value = st.text_input(f"custom value to fill missing values in '{column}'")
                    if st.buttom(f"fill missing valies in'{column}' with custom value"):
                        if custom_value:
                            df[column].fillna(custom_value, inplace=True)
                            st.session_state['df'] = df
                            st.success(f"missing values in'{column}' filled with custom value.")
                        else:
                            st.warning('please provide a custom value.')
                
                    # Iterative Imputation (MICE)
                    if st.button(f"Apply Iterative Imputation for '{column}'"):
                        imputer = IterativeImputer()
                        df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
                        st.session_state['df'] = df_imputed
                        st.success(f"Iterative Imputation applied successfully.")
        st.write(missing_value)


        if these_has_duplicateds_values:
                st.write("### Duplicate Values")
                st.write(f"**Number of duplicate rows:** {duplicate_count}")
                
                if st.button("Remove Duplicate Rows"):
                    df = df.drop_duplicates()
                    st.session_state['df'] = df
                    st.success("Duplicate rows removed successfully.")

                    duplicate_count = df.duplicated().sum()
                    st.write(duplicate_count)

        show_details = st.checkbox("Show Details")

        if show_details:
            st.write("### Basic Information")
            st.write(f"**Number of columns:** {df.shape[1]}")
            st.write(f"**Column names:** {list(df.columns)}")

            st.write("### Column Data Types")
            st.write(df.dtypes)

            st.write("### Missing Values")
            st.write(missing_value[missing_value > 0])

            st.write("### Duplicate Values")
            st.write(f"**Number of duplicate rows:** {duplicate_count}")























