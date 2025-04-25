import streamlit as st
import pandas as pd
import tempfile
import os

def process_files(file_paths):
    # Sample processing logic (replace with your actual logic)
    dfs = []
    for path in file_paths:
        df = pd.read_csv(path)
        dfs.append(df)
    final_df = pd.concat(dfs)
    return final_df

st.title("Folder File Processor to Excel")

uploaded_files = st.file_uploader("Upload multiple CSV files", type=['csv'], accept_multiple_files=True)

if uploaded_files:
    with tempfile.TemporaryDirectory() as temp_dir:
        file_paths = []
        for file in uploaded_files:
            temp_path = os.path.join(temp_dir, file.name)
            with open(temp_path, "wb") as f:
                f.write(file.read())
            file_paths.append(temp_path)

        result_df = process_files(file_paths)

        output_path = os.path.join(temp_dir, "output.xlsx")
        result_df.to_excel(output_path, index=False)

        with open(output_path, "rb") as f:
            st.download_button("Download Excel Result", f, file_name="result.xlsx")
