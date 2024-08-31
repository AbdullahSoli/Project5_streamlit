import streamlit as st
from streamlit_option_menu import option_menu
import joblib

#model = joblib.load('your_model.joblib')

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
    
    with st.form("prediction_form"):
        provider = st.text_input('Provider')
        level = st.selectbox('Level', ['Beginner', 'Intermediate', 'Advanced'])
        type_ = st.selectbox('Type', ['Online', 'In-Person'])
        duration_weeks = st.number_input('Duration / Weeks', min_value=1, max_value=52)

        submit_button = st.form_submit_button(label='Predict')

    if submit_button:
        input_data = [[provider, level, type_, duration_weeks]]
        
        prediction = model.predict(input_data)
        
        st.write(f'The prediction result is: {prediction[0]}')
