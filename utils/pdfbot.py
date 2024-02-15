import streamlit as st 
from streamlit_chat import message
import time
from helpers.helpers import Helper
from helpers.pdf_handler import PdfHandler
from helpers.vectorstore import VectorStore
from helpers.get_qa_chain import get_conversation_chain
helper=Helper()
pdfhandler=PdfHandler()
vectorstore=VectorStore()

def pdfbot():
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if 'done' not in st.session_state:
        st.session_state.done=False
    st.header("Chat with books")
    if st.session_state.credentials:
        with st.expander("Uploads files"):
            uploaded_file=st.file_uploader("Files",type='pdf')
            if uploaded_file is not None:
                chat=st.button("Chat")
                if chat:
                    with st.spinner("Progress"):
                       
                        st.write(f"{uploaded_file.name} loaded successfully.")
                        text=pdfhandler.get_pdf_text(uploaded_file)
                        chunks=pdfhandler.get_text_chunks(text)
                        vectorstores=vectorstore.embeddings(uploaded_file,chunks)
                        
                        st.session_state.conversation = get_conversation_chain(vectorstores)
                        
                        
                        st.session_state.done=True
        if st.session_state.done:
            user_question = st.chat_input("Ask Question about your files.")
            if user_question:
                handel_userinput(user_question)
            
                
    else:
        st.error("Please first login to proceed")
        st.stop()
        

def handel_userinput(user_question):
    
    response = st.session_state.conversation({'question':user_question})
    st.session_state.chat_history = response['chat_history']

    # Layout of input/response containers
    response_container = st.container()

    with response_container:
        for i, messages in enumerate(st.session_state.chat_history):
        
            if i % 2 == 0:
                message(messages.content, is_user=True, key=str(i),avatar_style="big-smile")
            else:
                message(messages.content, key=str(i),avatar_style="big-ears")

