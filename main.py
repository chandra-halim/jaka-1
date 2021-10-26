# app.py
import home
import plan
import login
import streamlit as st

PAGES = {
    "Home"  : home,
    "Login" : login,
    "Plan"  : plan,
}

st.set_page_config(
    page_title='JAKA',
    page_icon=':diamond:',
    layout='wide',
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help':
            'https://google.com',
        'Report a bug':
            'https://instagram.com',
        'About':
            "# This is a header. This is an *extremely* cool app!"
    }
)

# hide_menu_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """

# st.markdown(hide_menu_style, unsafe_allow_html=True)

st.sidebar.title('JAKA')
st.sidebar.info('Jadwal Aman Kuliah Aman')
selected = st.sidebar.selectbox('GO TO', PAGES.keys())
page = PAGES[selected]

if page != login:
    page.app()

else:
    user_login = page.app()
    if user_login['agree'] & user_login['login']:
        st.sidebar.balloons()
