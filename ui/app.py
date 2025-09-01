import streamlit as st
st.title("TPM Storyteller - MVP")
st.write("Hello! This is my first prototype dashboard")
status = st.text_area("Paste a project update here:")
if st.button("summarize"):
    st.write("Executive Summary:")
    st.write(f"{status[:75]}...(summary coming soon)")