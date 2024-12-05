import streamlit as st

st.header("Xin chào nhóm vui vẻ!")
st.image('logo.png')

st.write('Bạn có thư giãn không?')
chill = st.checkbox('Tôi là người thư giãn!')
if chill:
    st.write('Tôi cũng thế <3')
not_chill = st.checkbox('Tôi không!')
if not_chill:
    st.write('Kệ bạn <3')

st.multiselect('Moods:', ['Happy', 'Sad', 'Down'])
