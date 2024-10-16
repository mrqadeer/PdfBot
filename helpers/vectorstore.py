
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import streamlit as st 

import os,pickle

from helpers.helpers import Helper
helper=Helper()



class VectorStore:
    def embeddings(self,files,text_chunks):
        os.makedirs("embeddings",exist_ok=True)
       
        api_key=st.session_state.apikey
        # creating the Vectore Store using Facebook AI Semantic search
        
        file_name=helper.get_file_name(files)
        try:
            embeddings = OpenAIEmbeddings(api_key=api_key)
            #embeddings=HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
            knowledge_base = FAISS.from_texts(text_chunks,embeddings)
                

        except EOFError as e:
                st.error("Issue with your file.")
        
                
    
        return knowledge_base
