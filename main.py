# main.py
import home
import schedule
import login
import streamlit as st

PAGES = {
    "Home": home,
    "Schedule": schedule,
    "Login SSO": login
}

st.set_page_config(page_title='JAKA', page_icon=":books:")

hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(hide_menu_style, unsafe_allow_html=True)

st.sidebar.title('Navigation')
selected = st.sidebar.selectbox('Go To', PAGES.keys())
page = PAGES[selected]
page.app()
