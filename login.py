# login.py
import streamlit as st

user_agreement = """
    1. User perlu memasukkan username dan password SSO sebagai persyaratan login pada SIAK-NG
    2. JAKA akan melakukan scraping untuk mengumpulkan informasi jadwal
    3. Halaman yang diakses oleh JAKA dalam melakukan scraping HANYA https://academic.ui.ac.id/main/Schedule/Index
    4. Dengan mencentang "Saya setuju" pada akhir halaman ini berarti User telah menyetujui seluruh poin di atas.
    """

user_login = {
    "username"  : "",
    "password"  : "",
    "agreement" : False,
    "login"     : False,
}

def app():
    st.subheader('User Agreement')
    st.markdown(user_agreement, unsafe_allow_html=True)
    st.info('Harap dibaca secara saksama User Agreement di atas sebelum menyetujuinya.')
    
    user_login['username']  = st.sidebar.text_input('Username', max_chars=20)
    user_login['password']  = st.sidebar.text_input('Password', type='password')
    user_login['agree'] = st.sidebar.checkbox('Saya telah membaca dan menyetujui User Agreement')
    user_login["login"] = st.sidebar.button('Login')
    
    return user_login
