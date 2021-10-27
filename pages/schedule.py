import streamlit as st

def app():
    c1, c2 = st.columns((3, 1))
    with c1:
        st.title('Course Schedule')
        with st.expander('Course 1'):
            selected_1 = st.radio('Pilih Jadwal',
                                    ('Senin (13.00-15.00) + Selasa (13.00-15.00)',
                                     'Senin (13.00-15.00) + Rabu (13.00-15.00)',
                                     'Pilih nanti dari rekomendasi JAKA'))
        with st.expander('Course 2'):
            selected_2 = st.radio('Pilih Jadwal',
                                    ('Senin (13.00-15.00) + Kamis (13.00-15.00)',
                                     'Senin (13.00-15.00) + Jumat (13.00-15.00)',
                                     'Pilih nanti dari rekomendasi JAKA'))
    with c2:
        st.subheader('Course Plan')
        st.info('Course 1 : '+selected_1)
        st.info('Course 2 : '+selected_2)
            