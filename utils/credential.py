import streamlit as st 
from helpers.helpers import Helper
helper=Helper()
def credential():
    if 'username' not in st.session_state:
        st.session_state.username=""
        
    if 'apikey' not in st.session_state:
        st.session_state.gemenikey=""
    if "credentials" not in st.session_state:
        st.session_state.credentials=False
        
    st.header("Login to Use Bot")
    with st.form("Hello"):
        user_name=st.text_input("Your Name",max_chars=20).title()
        api_key=st.text_input("Your API Key",type='password')
        submit=st.form_submit_button("Login")
    if len(user_name)>=3 and len(api_key) and submit:
        st.subheader(f"Welcome {user_name}")
        st.session_state.username=user_name
        st.session_state.apikey=api_key
        
        st.session_state.credentials=True
    else:
        st.warning("Fill the fields correctly.")