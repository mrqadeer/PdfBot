import streamlit as st 
def credetial():
    if 'username' not in st.session_state:
        st.session_state.username=""
        
    if 'gemenikey' not in st.session_state:
        st.session_state.gemenikey=""
        
    st.markdown("## Login to Use Bot")
    with st.form("Hello"):
        user_name=st.text_input("Your Name",max_chars=20).title()
        gemeni_api_key=st.text_input("Your Gemeni API Key",type='password')
        submit=st.form_submit_button("Login")
        if len(user_name)>=3 and len(gemeni_api_key) and submit:
            st.write(f"Welcome {user_name}")
            st.session_state.username=user_name
            st.session_state.gemenikey=gemeni_api_key
            