import streamlit as st

check_u = 'admin'
check_p = 'admin'

def auth(username, password):
    if username == check_u and password == check_p:
        st.success('Login Successful')
    else:
        st.warning('Login Unsuccessful')
    return True

def app():
    st.title('Halo, dari Jaka')

    with st.form('login_form', clear_on_submit=True):
        u = st.text_input('Username', max_chars=30)
        p = st.text_input('Password', type='password', max_chars=30)
        is_agree = st.checkbox('Saya telah membaca dan menyetujui Kebijakan Privasi JAKA')
        is_login = st.form_submit_button('Login')

    if is_agree and is_login:
        return auth(u, p)
    else:
        return False