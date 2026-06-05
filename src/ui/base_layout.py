import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #0A0C10 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#1F242D !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #0A0C10 !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        # @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        # @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Lobster&family=Pacifico&family=Playwrite+AU+VIC+Guides&family=Rubik+Glitch&display=swap');        
        

                
         /* Hide Top Bar of streamlit */
                
            # #MainMenu, footer, header {
            #     visibility: hidden;
            # }
                
            .block-container {
                padding-top:1.5rem !important;    
            }
                
            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                # letter-spacing: 5px;
            }

                
            h1 {
                # font-family: 'Climate Crisis', sans-serif !important;
                font-family: 'Pacifico', cursive !important;
                font-size: 3.5rem !important;
                line-height: 1.1 1important;
                margin-bottom: 0rem !important;
                letter-spacing: 5px;
            }
                

            h2 {
                # font-family: 'Climate Crisis', sans-serif !important;
                font-family: 'Pacifico', cursive !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                letter-spacing: 5px;
            }
                
            h3, h4, p {
                # font-family: 'Outfit', sans-serif; 
                font-family: 'Pacifico', cursive !important;
                # letter-spacing: 5px;  
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #FFA200 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                
                
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #770DC7 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: #444445 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            
                }

            button:hover{
                transform :scale(1.05)}

            
            # <h1 style='
            #     text-align: center;
            #     color: #FFFFFF;
            #     letter-spacing: 5px;
            # '>
            #     Login using password
            # </h1>
  

                """
            ,unsafe_allow_html=True)