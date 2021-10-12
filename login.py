import streamlit as st
# import streamlit.components.v1 as components

user_agreement = """
    1. User perlu memasukkan username dan password SSO sebagai persyaratan login pada SIAK-NG
    2. JAKA akan melakukan scraping untuk mengumpulkan informasi jadwal
    3. Halaman yang diakses oleh JAKA dalam melakukan scraping HANYA https://academic.ui.ac.id/main/Schedule/Index
    4. Dengan mencentang "Saya setuju" pada akhir halaman ini berarti User telah menyetujui seluruh poin di atas.
    """

def app():
    st.subheader('User Agreement')
    st.markdown(user_agreement, unsafe_allow_html=True)
    st.info('Harap dibaca secara saksama User Agreement di atas sebelum menyetujuinya')
    return st.checkbox('Saya setuju')
