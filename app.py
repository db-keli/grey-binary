import streamlit as st
from grayToBinary import gray_to_binary
from grayToBinary import binary_to_gray
css = """
<style>
body {
    background-image: url('./image.jpeg'); 
    background-size: cover;
}
>/style>
"""

st.set_page_config(page_title="Background Image Example")
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

hide_streamlit_style = """
            <style>
                header{visibility:hidden;}
                .main {
                    margin-top: -120px;
                    padding-top:10px;
                }
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("Grey To Binary Code Converter")

courses_col, student_col = st.columns(2)
with courses_col:
    st.subheader("Grey Code To Binary Code")
    grey = st.text_input("Grey Code")
    st.write("Binary Code")
    if grey:
        binary = gray_to_binary(grey)
        st.subheader(binary)
                

with student_col: 
    st.subheader("Binary Code To Grey Code")
    binary = st.text_input("Binary Code")
    st.write("Grey Code")
    if binary:
        grey = binary_to_gray(binary)
        st.subheader(grey)


with st.expander('Help'):
    st.write("Grey")
