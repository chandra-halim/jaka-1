import streamlit as st
from pages import home, login, error, schedule

st.set_page_config(
    page_title="JAKA",
    page_icon="random",
    layout="wide"
)

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""

st.markdown(hide_menu_style, unsafe_allow_html=True)
page_list = [
    'Home'
    ,'Login'
    ,'Schedule'
    # ,'View Plan'    
]

h1, h2 = st.columns((5, 1))

with h1: # Kolom kiri untuk logo
    st.write(" ")
    st.image(
        'https://i.ibb.co/yP2wjhW/jaka-02.png',
        width=100
    )

with h2: # Dropdown menu
    menu = st.selectbox(
        label='Go To',
        options=page_list,
    )

if menu == 'Home':
    home.app()
elif menu == 'Schedule':
    schedule.app()
else:
    error.app(307)
