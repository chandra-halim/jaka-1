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

st.sidebar.title('Navigation')
route = st.sidebar.selectbox('Go To', PAGES.keys())
route.app()