# File Processor Web App

This is a simple Streamlit web app that takes multiple uploaded CSV files, processes them, and returns a single Excel file as output.

## Features

- Upload multiple CSV files
- Combine and process them (custom logic inside `process_files`)
- Download the result as an Excel file

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
