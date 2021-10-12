# app.py
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

st.sidebar.title('JAKA')
st.sidebar.info('Jadwal Aman Kuliah Aman')
selected = st.sidebar.selectbox('GO TO',PAGES.keys())
page = PAGES[selected]

if page != login:
    page.app()

elif page.app() == True:
    st.sidebar.balloons()
