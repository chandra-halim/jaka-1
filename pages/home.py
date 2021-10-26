import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
def app():
    c1, c2 = st.columns(2)
    
    with c1:
        body = st.container()
        for i in range(8):
            body.write(' ')
        body.title("JAKA", 'get-started')
        about_text = """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
            Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        """
        body.write(about_text)
        for i in range(2):
            body.write(' ')
            
        st.markdown('''
            <style>
            .button {
              background-color: #f72585;
              border: none;
              color: white;
              padding: 15px 32px;
              text-align: center;
              text-decoration: none;
              display: inline-block;
              font-size: 16px;
              margin: 4px 2px;
              cursor: pointer;
              width: 50%;
            }

            .button:hover {
              box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
            }
            </style>
            <button class="button" onclick="alert('Hello world!')"> Get Started </button>
        ''', unsafe_allow_html=True)
        started = st.button("Get Started", help='klik untuk memulai!')
        if started:
            st.balloons()
            st.success('Cieee, udah siap nih buat mulai')
    with c2:
        lottie_file = load_lottiefile("assets/schedule.json")  # replace link to local lottie file
        # lottie_file = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_ok9cq9zj.json")

        st_lottie(
            lottie_file,
            speed=1,
            reverse=False,
            loop=True,
            quality="high", # small; medium ; high
            renderer="svg", # svg; canvas
            height=None,
            width=None,
            key="lottie-schedule",
        )
