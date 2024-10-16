
import streamlit as st 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

def get_conversation_chain(vetorestore):
    """
    This function creates a ConversationalRetrievalChain using a ChatGoogleGenerativeAI LLM, a given VectorStore as a retriever, and a ConversationBufferMemory.

    :param vetorestore: A VectorStore to be used as a retriever
    :return: A ConversationalRetrievalChain
    """
    api_key=st.session_state.apikey
    llm=ChatGoogleGenerativeAI(model='gemini-1.5-pro-002',api_key=api_key)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vetorestore.as_retriever(),
        memory=memory
    )
    return conversation_chain       

