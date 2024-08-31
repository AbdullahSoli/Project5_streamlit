import streamlit as st
from streamlit_option_menu import option_menu
import joblib
import pandas as pd
import plotly.express as px

# Load the model
#model = joblib.load('your_model.joblib')

# Load the data
#df = pd.read_csv("cleaned_coursera_dataset2.csv")

# Create plots
#fig_ratings = px.histogram(df, x='Rating', nbins=20, title='Distribution of Ratings', height=600)
#fig_providers = px.histogram(df.nlargest(60, 'Reviews'), x='Provider', nbins=20, title='Distribution of Providers', color='Provider', height=600)
#fig_levels = px.histogram(df, x='Level', nbins=20, title='Distribution of course Levels', color='Level', height=600)
#fig_reviews = px.histogram(df, x='Reviews', nbins=6, title='Distribution of Reviews', height=600)
#fig_types = px.histogram(df, x='Type', nbins=30, title='Distribution of course Types', color='Type', height=500)
#fig_duration = px.histogram(df, x='Duration', nbins=20, title='Distribution of course Durations', color='Duration', height=500)
#df_top_10 = df.sort_values(by='Reviews', ascending=False).head(10)
#fig_reviews_course = px.histogram(df_top_10, x='Course Title', y='Reviews', color='Course Title', title='Number of Reviews per Course', height=600)
#fig_duration_pie = px.pie(df['Duration'].value_counts().reset_index(), names='index', values='Duration', title='Distribution of Course Durations', width=1000, height=600)
#fig_type_provider = px.scatter(df[df['Provider'].isin(df['Provider'].value_counts().nlargest(10).index)], x='Type', y='Provider', color='Provider', title='Type of Course by Provider (Top 10 Providers by Count)', width=1000, height=600)
#fig_rating_provider = px.histogram(df[df['Provider'].isin(df['Provider'].value_counts().nlargest(5).index)], x='Provider', y='Reviews', title='Reviews VS Provider', color='Provider', height=600)
#fig_reviews_rating = px.scatter(df, x='Rating', y='Reviews', title='Number of Reviews by Rating', color='Rating')
#fig_duration_top_courses = px.scatter(df_top_10, x='Course Title', y='Duration', title='Duration of Top 10 Courses', color='Duration / Weeks', height=600)

# Streamlit layout
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Home", "A Guide to Coursera's Premier Data  Courses", "K-Means Clustering","Prediction"],
        icons=["house", "file-earmark-text", "file-earmark-text"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    st.title("Welcome to Home Page")
    st.write("This is the home page.")

elif selected == "A Guide to Coursera's Premier Data  Courses":
    st.title("Coursera Data Analysis")
    
    st.subheader("Univariate Analysis")
    #st.plotly_chart(fig_ratings)
    st.image("chart1.png")
    st.write("Most Coursera courses have ratings between 4 and 5, indicating that it is a valuable platform for taking courses.")
    
    #st.plotly_chart(fig_providers)
    st.image("chart2.png")
    st.write("IBM demonstrates its expertise by offering courses across a wide range of tracks.")
    
    #st.plotly_chart(fig_levels)
    st.image("chart3.png")
    st.write("We can indicate that most Coursera users are beginners.")
    
    #st.plotly_chart(fig_reviews)
    st.image("chart4.png")
    st.write("Most of the course ratings fall between 0 and 50k.")
    
    #st.plotly_chart(fig_types)
    st.image("chart5.png")
    st.write("Since most users are beginners, the courses have the highest enrollment numbers.")
    
    #st.plotly_chart(fig_duration)
    st.image("chart6.png")
    st.write("Users prefer to take courses that do not exceed three months in duration.")
    
    st.subheader("Bivariate/Multivariate Analysis")
    
    st.write("**Chart 1: Level vs. Type**")
    #st.pyplot(plt.figure().add_subplot(111).bar(df.groupby(['Type', 'Level']).size().unstack(fill_value=0).index, df.groupby(['Type', 'Level']).size().unstack(fill_value=0).values))
    st.image("chart7.png")
    st.write("The chart shows a dominant focus on 'Beginner' level courses in 'Course' and 'Specialization' types.")
    
    #st.plotly_chart(fig_provider_rating)
    st.image("chart8.png")
    st.write("Most IBM enrollees have liked the courses.")
    
    #st.plotly_chart(fig_reviews_course)
    st.image("chart9.png")
    st.write("The 'Python for Everybody' course has the highest number of reviews, indicating its popularity among learners compared to other courses.")
    
    #st.plotly_chart(fig_duration_pie)
    st.image("chart10.png")
    st.write("A three-month period is the most preferred duration for courses.")
    
    #st.plotly_chart(fig_type_provider)
    st.image("chart11.png")
    st.write("Professional certificates are not offered by many companies.")
    
    #st.plotly_chart(fig_rating_provider)
    st.image("chart12.png")
    st.write("Most of the top providers by reviews are universities.")
    
    #st.plotly_chart(fig_reviews_rating)
    st.image("chart12.png")
    st.write("The majority of courses on Coursera have high ratings.")
    
    #st.plotly_chart(fig_duration_top_courses)
    
elif selected == "K-Means Clustering":
    st.title("K-Means Clustering")
    st.image("Silhouette Score")
    st.image("Silhouette plot for the various cluster")
    st.image("cluster_non_PCA")
    st.image("Density")
    st.image("distribution of clusters by provider")
    
   
elif selected == "Prediction":
    st.title("Prediction Page")
    
    with st.form("prediction_form"):
        provider = st.text_input('Provider')
        level = st.selectbox('Level', ['Beginner', 'Intermediate', 'Advanced', 'Mixed'])
        type_ = st.selectbox('Type', ['Professional Certificate', 'Specialization', 'Course'])
        duration_weeks = st.selectbox('Duration Range by Weeks', ['1 - 4', '4 - 12', '12 - 24'])
        rating = st.selectbox('Rating', ['Excellent rating', 'Average rating', 'Above average rating', 'Low rating', 'Very low rating'])
        reviews = st.number_input('Numbers of Reviews')


        submit_button = st.form_submit_button(label='Predict')

    if submit_button:
        input_data = [[provider, level, type_, duration_weeks, rating, reviews]]
        
        prediction = model.predict(input_data)
        
        st.write(f'The prediction result is: {prediction[0]}')
