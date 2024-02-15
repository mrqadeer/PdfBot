import os
import streamlit as st
class Helper:
    def get_file_name(self,pdf_file):
        file_name=os.path.splitext(pdf_file.name)[0]

        return file_name
    # def setup_api(self):
    #     gemeni_key=st.session_state['gemenikey']
    #     with open('.env','a') as file:
    #         file.write("'")
    #         file.write(gemeni_key)
    #         file.write("'")