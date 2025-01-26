# doc_summarizer

Description:
Document Summarizer with LangChain and Streamlight:
This Streamlit application offers a user-friendly interface for generating concise summaries of uploaded documents. It uses the LangChain framework and ChatGroq for efficient text summarization. The application supports various formats, including PDFs, Word documents (.docx), and text files (.txt).

Modules and Their Roles:
1. Streamlit (Frontend):

  This module offers an interactive and user-friendly interface for uploading files.
  Accepts document uploads through the st.file_uploader() component.
  Displays the generated summary using st.subheader() and st.write().

2. doc_summarizer Module (Backend):

   Processes the uploaded document by identifying its format (PDF, DOCX, or TXT).
   Extracts the text content using:
   PyPDF2 for PDFs.
   docx2txt for Word documents.
   Native text decoding for .txt files.
   Leverages LangChain's create_stuff_documents_chain and ChatGroq LLM to generate a summary.
   Ensures modular and reusable backend logic for handling unsupported file types.

3. LangChain Framework:

   Orchestrates the summarisation pipeline by combining the document loader, prompts, and LLM integration.
   Employs a structured prompt template to ensure the output is concise (100–150 words).

4.PyPDF2 & docx2txt:

   PyPDF2: Extracts textual data from uploaded PDFs.
   docx2txt: Processes Word documents and extracts their text content.

Key Features:

   File Format Support: Seamlessly handles PDF, DOCX, and TXT files.
   Powered by LLMs: Utilizes ChatGroq for advanced natural language summarisation.
   Error Handling: Provides user feedback if unsupported file types are uploaded.
   Simple Interface: Allows users to upload a document and view its summary with minimal effort.


How It Works:
1. Upload the Document:
   The user uploads a PDF, DOCX, or TXT file through the Streamlit interface.

2. Process the Document:
   The application determines the file type and extracts its content using PyPDFLoader, Docx2txtLoader, or native text reading.

3. Generate a Summary:
   The text is passed to the doc_summarizer module, which processes it using LangChain and the ChatGroq LLM.

4. Display the Output:
   The generated summary is displayed interactively within the application.

Potential Use Cases:
   Research papers, legal documents, and report summaries.
   Streamlining text analysis for quick insights.
   Simplifying workflows that involve reviewing long documents.
This tool is ideal for users seeking efficient and AI-powered summarization with a clean and easy-to-use interface.

