from langchain.schema import Document
import docx2txt
from langchain.chains.llm import LLMChain
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.summarize import load_summarize_chain

import PyPDF2
from langchain.chains.combine_documents import create_stuff_documents_chain
API_key="******"#put your api key

class unsupported_document_type(Exception):
    """Raised when an for unsupported document type is given as input."""
    pass


def load_file(uploaded_file):
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        all_text = ""
        for page in pdf_reader.pages:
            all_text += page.extract_text()

        docs=[Document(page_content=all_text)]

        return docs
    
    elif file_name.endswith('.docx'):
        text = docx2txt.process(uploaded_file)
        docs=[Document(page_content=text)]

        return docs
    
    elif file_name.endswith('.txt'):
        content = uploaded_file.read().decode("utf-8")  # Decode from bytes to string
        docs = [Document(page_content=content)]  # Wrap the content into a Document object
        return docs


class doc_summarizer():
    @staticmethod
    def doc_summarizer(uploaded_file):
        try:
            filename=uploaded_file.name.lower()
            if not filename.endswith((".pdf", ".txt", ".docx")):
                raise unsupported_document_type
            
            else:
                context=load_file(uploaded_file)
                prompt = ChatPromptTemplate.from_messages(
    [("system", "Write a 100-150 words summary of the following:\\n\\n{context}")]
)
                llm = ChatGroq(api_key=API_key,model="llama3-8b-8192")
                chain = create_stuff_documents_chain(llm, prompt)
                result = chain.invoke({"context": context})
                return result
        except unsupported_document_type:
            return "Unsupported document type, Please upload the correct file format."

# res=doc_summarizer.doc_summarizer(r"C:\Users\Tasneem Fathima\Downloads\AI BASED RECOMMENDATION SYSTEM.pptx")
# print(res)





