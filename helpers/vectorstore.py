
from langchain.embeddings import HuggingFaceEmbeddings,OpenAIEmbeddings
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
        
        
        if os.path.exists(f"embeddings/{file_name}.pkl"):
            try:
                with open(f"embeddings/{file_name}.pkl", "rb") as rf:
                    knowledge_base = pickle.load(rf)
            except FileNotFoundError as fe:
                st.warning(f"File not found")
            else:
                st.info("Vector stored loaded successfully.")
        else:
            try:
                # embeddings = OpenAIEmbeddings(api_key=api_key)
                embeddings=HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
                knowledge_base = FAISS.from_texts(text_chunks,embeddings)
                with open(f"embeddings/{file_name}.pkl", "wb") as wf:
                    pickle.dump(knowledge_base, wf)

            except EOFError as e:
                st.error("Issue with your file.")
            else:
                st.info("Vector stored")
                
    
        return knowledge_base
