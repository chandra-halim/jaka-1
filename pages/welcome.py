import streamlit as st
import time

def new():
    with st.spinner():
        bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            bar.progress(percent_complete + 1)
        # bar.progress(0)        
    st.session_state["loading"] = False
    
def old():
    pass