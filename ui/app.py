import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
st.title("TPM Storyteller - MVP")
st.write("Hello! This is my first prototype dashboard")
from data_ingestion.ingest_excel import load_excel
from ai_processing.process_data import compute_summary
from ai_processing.summarizer import summarize_text
# Upload Excel file
uploaded_file = st.file_uploader("Upload your project Excel", type=["xlsx"])
if uploaded_file:
    # Load Excel into dataframe
    df = load_excel(uploaded_file)
   # st.write("Columns detected in Excel:")
   # st.write(df.columns.tolist())
    if df is not None:
        st.write("### Project Data")
        st.dataframe(df)
        # Compute basic summary metrics
        summary = compute_summary(df)
        st.write("### Summary")
        st.json(summary)
        # Prepare text for AI Summarization
        text_data = " ".join(df.astype(str).values.flatten())
        if st.button("Generate Executive Summary"):
            summary_text = summarize_text(text_data)
            st.subheader("Executive Summary")
            st.write(summary_text)
