import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Home", "Page 1", "Page 2"],
        icons=["house", "file-earmark-text", "file-earmark-text"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    st.title("Welcome to Home Page")
    st.write("This is the home page.")
elif selected == "Page 1":
    st.title("Page 1")
    st.write("This is Page 1.")
elif selected == "Page 2":
    st.title("Page 2")
    st.write("This is Page 2.")
