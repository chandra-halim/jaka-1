# app1.py
import streamlit as st
def app():
    p1 = '''
        <p style="color:blue;font-size:46px;">
            I'm a big, blue, <strong>strong</strong> paragraph
        </p>
        '''
    st.title('APP1')
    st.color_picker('Pick A Cplor', '#00f900')
    st.markdown(p1, unsafe_allow_html=True)
    st.write('Welcome to app1')
