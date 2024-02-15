import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config("PDF Bot",page_icon=":book:")
from utils.credential import credetial

class MyApp:
    """
    This class is main class of this application
    """
    # Constructor of class
    def __init__(self):
        
        self.apps = []
        
    def add_app(self, title, function):
        self.apps.append({"title": title, "function": function})


    def run(self):
        """
        This method run the streamlit app
        """
        with st.sidebar:
            app = option_menu(
                menu_title='PDF Bot',
                options=['Credentials', 'Chat'],
                icons=['house-heart', 'data'],
                menu_icon='chat-text-fill',
                default_index=0,

                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "20px"},
                    "nav-link": {"color": "white", "font-size": "20px", 
                                 "text-align": "left", "margin": "0px",
                                 "--hover-color": "magenta"},
                    "nav-link-selected": {"background-color": "#02ab21"}, })
      
        if app=="Credentials":
            credetial()
            



if __name__ == "__main__":
    app = MyApp()  # Object of classa
    app.run()
