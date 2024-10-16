
from langchain_google_genai import GoogleGenerativeAIEmbeddings


from langchain.vectorstores import FAISS
import streamlit as st 

import os,pickle

from helpers.helpers import Helper
helper=Helper()



class VectorStore:
    def embeddings(self,text_chunks):
        
       
        """
        This function calculates the embeddings for the given text chunks using GoogleGenerativeAIEmbeddings and FAISS.

        :param text_chunks: List of text chunks for which embeddings need to be calculated
        """
        api_key=st.session_state.apikey
        # creating the Vectore Store using Facebook AI Semantic search
        
        try:
            embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",
                                                      google_api_key=api_key)
            #embeddings=HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
            knowledge_base = FAISS.from_texts(text_chunks,embeddings)
            return knowledge_base
        except Exception as e:
            st.error(f'Error: {e}')
        
                
    
        
