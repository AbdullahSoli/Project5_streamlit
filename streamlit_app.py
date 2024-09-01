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
        "",
        ["Home", "A Guide to Coursera's Premier Data Courses", "K-Means Clustering", "Prediction"],
        icons=["house", "file-earmark-text", "file-earmark-text"],
        menu_icon="cast",
        default_index=0,
    )
def get_readable_result(prediction):
    result = {
                0:"Not a popular course, not recommended", 
                1: "This is a popular course, recommended!", 
                2: "Average popularity, could be useful",
                }
    
    return result[prediction]

if selected == "Home":
    st.title("Analyzing and Categorizing Coursera Data Courses Using K-means Clustering")
    
    
    st.write("""
                 In this project, we conducted a comprehensive analysis of data courses available on the Coursera platform. We developed a machine learning model using the K-means clustering algorithm to categorize the courses into distinct groups based on their features.

                  Following the clustering process, we performed an in-depth analysis of the resulting clusters to uncover patterns and trends. We extracted valuable insights from the clustered data, which helped us understand the distribution and characteristics of different courses. Additionally, we explored how various factors influence course categorization and identified key attributes that drive clustering results.

                  Our findings provide a clearer understanding of the course offerings on Coursera and can be used to make informed decisions regarding course selection and future recommendations.
                   """)

elif selected == "A Guide to Coursera's Premier Data Courses":
    st.title("Coursera EDA Analysis")
    st.write("""
                 In this analysis, we delve into the characteristics and trends of Coursera courses through various levels of examination. 
                 Our univariate analysis explores individual aspects such as course ratings, enrollment numbers, and user preferences regarding course duration. 
                 By visualizing data through multiple charts, we uncover key insights about the general quality and distribution of Coursera courses. Moving on to bivariate and multivariate analysis, 
                 we investigate the relationships between different factors such as course levels, types, and user feedback. 
                 This deeper analysis sheds light on the patterns and preferences of Coursera users and the performance of different course providers.
                   """)
    st.subheader("Univariate Analysis")
    st.image("img/chart1.png")
    st.write("Most Coursera courses have ratings between 4 and 5, indicating that it is a valuable platform for taking courses.")
    st.image("img/chart2.png")
    st.write("IBM demonstrates its expertise by offering courses across a wide range of tracks.")
    st.image("img/chart3.png")
    st.write("We can indicate that most Coursera users are beginners.")
    st.image("img/chart4.png")
    st.write("Most of the course ratings fall between 0 and 50k.")
    st.image("img/chart5.png")
    st.write("Since most users are beginners, the courses have the highest enrollment numbers.")
    st.image("img/chart6.png")
    st.write("Users prefer to take courses that do not exceed three months in duration.")
    
    st.subheader("Bivariate/Multivariate Analysis")
    st.write("**Chart 1: Level vs. Type**")
    st.image("img/chart7.png")
    st.write("The chart shows a dominant focus on 'Beginner' level courses in 'Course' and 'Specialization' types.")
    st.image("img/chart8.png")
    st.write("Most IBM enrollees have liked the courses.")
    st.image("img/chart9.png")
    st.write("The 'Python for Everybody' course has the highest number of reviews, indicating its popularity among learners compared to other courses.")
    st.image("img/chart10.png")
    st.write("A three-month period is the most preferred duration for courses.")
    st.image("img/chart11.png")
    st.write("Professional certificates are not offered by many companies.")
    st.image("img/chart12.png")
    st.write("Most of the top providers by reviews are universities.")
    st.image("img/chart12.png")
    st.write("The majority of courses on Coursera have high ratings.")

    st.write("""
                Our analysis reveals that Coursera is a platform highly favored by users, particularly beginners, who tend to prefer shorter courses with high ratings. 
                The insights from our univariate and bivariate/multivariate analyses highlight the dominance of beginner-level courses and the significant role of established institutions like IBM and universities in providing quality education. 
                Additionally, the preference for shorter course durations and the high ratings across most courses underscore the effectiveness of Coursera's offerings. 
                This comprehensive examination provides valuable information for users seeking to make informed decisions about their course selections and for providers aiming to optimize their course offerings.
                   """)

elif selected == "K-Means Clustering":
    st.title("K-Means Clustering")
    st.image("img/Silhouette Score.png")
    st.image("img/Silhouette plot for the various cluster.png")
    st.image("img/cluster_non_PCA.png")
    st.image("img/Density.png")
    st.image("img/distribution of clusters by provider.png")

elif selected == "Prediction":
    
    st.title("Prediction Page")
    
    with st.form("prediction_form"):
        rating = st.number_input("Rating (1-5):", min_value=0.0)
        reviews = st.number_input("Total Reviews:", min_value=0)
        duration_weeks = st.number_input("Duration in weeks:", min_value=0)

        submit_button = st.form_submit_button(label='Predict')

    if submit_button:

        # Prepare data to send to FastAPI
        cors_data = {
            "rating": rating,
            "reviews": reviews,
           "duration_weeks": duration_weeks
        }

        try:
            # Send data to FastAPI
            response = requests.post("https://team-pirates-project-5.onrender.com/predict/", json=cors_data)
            response.raise_for_status()  # Will raise an HTTPError for bad responses

            # Extract and display prediction
            prediction = response.json().get("prediction", "No prediction found")

            prediction = get_readable_result(prediction)

            st.write(f"Prediction: {prediction}")
            
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
