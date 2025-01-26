import streamlit as st
from doc_summarizer import doc_summarizer
import PyPDF2

st.title("Document Summarizer with Groq")

st.write("Upload a document (PDF, DOCX, or TXT)")

uploaded_file = st.file_uploader(" ", type=["pdf", "docx", "txt"])
if uploaded_file:
    file_name = uploaded_file.name.lower()
    summary=doc_summarizer.doc_summarizer(uploaded_file)
    st.subheader("Generated Summary:")
    st.write(summary)
    
