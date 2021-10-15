# app1.py
import streamlit as st
def app():
    p1 = '''
        <h1>
            I'm a big, blue, <strong>strong</strong> paragraph
        </h1>
        '''
    st.title('APP1')
    st.color_picker('Pick A Cplor', '#00f900')
    st.markdown(p1, unsafe_allow_html=True)
    st.write('Welcome to app1')
