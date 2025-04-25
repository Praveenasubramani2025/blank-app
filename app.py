import streamlit as st
import pandas as pd
import tempfile
import os

def process_files(file_list):
    # Example: just read CSV files and combine
    dfs = []
    for file in file_list:
        df = pd.read_csv(file)
        dfs.append(df)
    final_df = pd.concat(dfs)
    return final_df

st.title("File Processor to Excel")

uploaded_files = st.file_uploader("Upload your files", accept_multiple_files=True, type=['csv'])

if uploaded_files:
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_paths = []
        for file in uploaded_files:
            path = os.path.join(temp_dir, file.name)
            with open(path, "wb") as f:
                f.write(file.read())
            temp_paths.append(path)

        df = process_files(temp_paths)
        output_excel = os.path.join(temp_dir, "output.xlsx")
        df.to_excel(output_excel, index=False)

        with open(output_excel, "rb") as f:
            st.download_button("Download Excel", f, file_name="result.xlsx")
