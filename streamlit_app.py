import streamlit as st
from streamlit_option_menu import option_menu
import joblib
import pandas as pd
import plotly.express as px
import requests

# Load the model (uncomment when you have your model file)
# model = joblib.load('your_model.joblib')

# Streamlit layout with sidebar menu
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Home", "A Guide to Coursera's Premier Data Courses", "K-Means Clustering", "Prediction"],
        icons=["house", "file-earmark-text", "file-earmark-text"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    st.title("Welcome to Home Page")
    st.write("This is the home page.")

elif selected == "A Guide to Coursera's Premier Data Courses":
    st.title("Coursera Data Analysis")
    
    st.subheader("Univariate Analysis")
    st.image("img/chart1.png")
    st.write("Most Coursera courses have ratings between 4 and 5, indicating that it is a valuable platform for taking courses.")
    st.image("chart2.png")
    st.write("IBM demonstrates its expertise by offering courses across a wide range of tracks.")
    st.image("chart3.png")
    st.write("We can indicate that most Coursera users are beginners.")
    st.image("chart4.png")
    st.write("Most of the course ratings fall between 0 and 50k.")
    st.image("chart5.png")
    st.write("Since most users are beginners, the courses have the highest enrollment numbers.")
    st.image("chart6.png")
    st.write("Users prefer to take courses that do not exceed three months in duration.")
    
    st.subheader("Bivariate/Multivariate Analysis")
    st.write("**Chart 1: Level vs. Type**")
    st.image("chart7.png")
    st.write("The chart shows a dominant focus on 'Beginner' level courses in 'Course' and 'Specialization' types.")
    st.image("chart8.png")
    st.write("Most IBM enrollees have liked the courses.")
    st.image("chart9.png")
    st.write("The 'Python for Everybody' course has the highest number of reviews, indicating its popularity among learners compared to other courses.")
    st.image("chart10.png")
    st.write("A three-month period is the most preferred duration for courses.")
    st.image("chart11.png")
    st.write("Professional certificates are not offered by many companies.")
    st.image("chart12.png")
    st.write("Most of the top providers by reviews are universities.")
    st.image("chart12.png")
    st.write("The majority of courses on Coursera have high ratings.")

elif selected == "K-Means Clustering":
    st.title("K-Means Clustering")
    st.image("Silhouette Score.png")
    st.image("Silhouette plot for the various cluster.png")
    st.image("cluster_non_PCA.png")
    st.image("Density.png")
    st.image("distribution of clusters by provider.png")

elif selected == "Prediction":
    st.title("Prediction Page")
    
    with st.form("prediction_form"):
        provider = st.selectbox('provider', ['IBM', 'Googel'])
        level = st.selectbox('Level', ['Beginner', 'Intermediate', 'Advanced', 'Mixed'])
        type_ = st.selectbox('Type', ['Professional Certificate', 'Specialization', 'Course'])
        duration_weeks = st.selectbox('Duration Range by Weeks', ['1 - 4', '4 - 12', '12 - 24'])

        submit_button = st.form_submit_button(label='Predict')

    if submit_button:
        # Prepare data to send to FastAPI
        cors_data = {
            "provider": provider,
            "level": level,
            "type": type_,
           "duration_Weeks": duration_weeks
        }

        try:
             Send data to FastAPI
            response = requests.post("https://api-project-0j0c.onrender.com/predict", json=cors_data)
            response.raise_for_status()  # Will raise an HTTPError for bad responses

             Extract and display prediction
            prediction = response.json().get("prediction", "No prediction found")
            st.write(f"Prediction: {prediction}")
            
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
