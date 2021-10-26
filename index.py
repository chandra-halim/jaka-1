import streamlit as st
from pages import home, login, error

st.set_page_config(
    page_title="JAKA",
    page_icon="random",
    layout="wide"
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
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
    """

st.markdown(hide_menu_style, unsafe_allow_html=True)

page_list = [
    'Home'
    ,'Login'
    # ,'Create Plan'
    # ,'View Plan'    
]

h1, h2 = st.columns((5, 1))

with h1: # Kolom kiri untuk logo
    st.write(" ")
    st.write(" ")
    st.image(
        'https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Gojek_logo_2019.svg/2560px-Gojek_logo_2019.svg.png',
        width=150
    )

with h2: # Dropdown menu
    menu = st.selectbox(
        label='Go To',
        options=page_list,
    )

if menu == 'Home':
    home.app()
else:
    error.app(307)

# Simulasi Loading sebelum ke Home Page
#     if "loading" not in st.session_state:
#         st.session_state["loading"] = False

#     if st.session_state["loading"] == False:
#         welcome.new()
#         st.session_state["loading"] = True
#         start = st.button("Get Started")
#     else:
#         start = True
#         welcome.old()

#     if start:
#         home.app()
