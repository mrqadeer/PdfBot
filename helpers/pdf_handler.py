from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
class PdfHandler:
    def get_pdf_text(self,pdf_docx):
        # Function to read PDF Files
        text = ""   
        pdf_reader = PdfReader(pdf_docx)
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    def get_text_chunks(self,texts):
        """
        :param texts: This function takes a list of documents for splitting
        :return: It returns the chunks of documents
        """

        # Splitting the text
        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n", "-."],
            chunk_size=10000,
            chunk_overlap=1000,
            length_function=len
        )

        # Making chunks
        chunks = text_splitter.split_text(texts)

        return chunks
