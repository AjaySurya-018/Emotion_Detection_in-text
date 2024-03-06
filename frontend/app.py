# Core Packages
import streamlit as st
import altair as alt
import plotly.express as px

# EDA Packages
import pandas as pd
import numpy as np
from datetime import datetime

# Load Model
from pyspark.sql import SparkSession
from pyspark.ml import PipelineModel

# Load Database Packages
from database import create_page_visited_table, add_page_visited_details, view_all_page_visited_details, create_emotionclf_table, add_prediction_details, view_all_prediction_details

# Load the PySpark model
spark = SparkSession.builder.appName("EmotionDetectionApp").getOrCreate()
model_path = "C:/Users/jaysa/OneDrive/Desktop/Emotion_Detection/backend/model"  # Update with the actual path where your model is saved
loaded_model = PipelineModel.load(model_path)

# Function to predict emotions using the loaded model
def predict_emotions(docx):
    predictions = loaded_model.transform(pd.DataFrame({"Text": [docx]}))
    prediction = predictions.select("class.result").rdd.flatMap(lambda x: x).collect()[0]
    probability = predictions.select("class.metadata.probability").rdd.flatMap(lambda x: x).collect()[0]
    return prediction, probability

emotions_emoji_dict = {"anger": "😠",  "fear": "😨😱",  "joy": "😂", "neutral": "😐", "sadness": "😔", "surprise": "😮"}

# Main Application
def main():
    st.title("Emotion Classifier App")
    menu = ["Home", "Monitor", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_page_visited_table()
    create_emotionclf_table()
    
    if choice == "Home":
        add_page_visited_details("Home")
        st.subheader("Emotion Detection in Text")

        with st.form(key='emotion_clf_form'):
            raw_text = st.text_area("Type Here")
            submit_text = st.form_submit_button(label='Submit')

        if submit_text:
            col1, col2 = st.columns(2)

            # Apply Function Here
            prediction, probability = predict_emotions(raw_text)
            
            add_prediction_details(raw_text, prediction, probability)

            with col1:
                st.success("Original Text")
                st.write(raw_text)

                st.success("Prediction")
                emoji_icon = emotions_emoji_dict[prediction]
                st.write("{}:{}".format(prediction, emoji_icon))
                st.write("Confidence:{}".format(probability))

            with col2:
                st.success("Prediction Probability")
                proba_df = pd.DataFrame({"emotions": [prediction], "probability": [probability]})
                fig = alt.Chart(proba_df).mark_bar().encode(x='emotions', y='probability', color='emotions')
                st.altair_chart(fig, use_container_width=True)

    elif choice == "Monitor":
        add_page_visited_details("Monitor")
        st.subheader("Monitor App")

        with st.expander("Page Metrics"):
            page_visited_details = pd.DataFrame(view_all_page_visited_details(), columns=['Page Name', 'Time of Visit'])
            st.dataframe(page_visited_details)

            pg_count = page_visited_details['Page Name'].value_counts().rename_axis('Page Name').reset_index(name='Counts')
            c = alt.Chart(pg_count).mark_bar().encode(x='Page Name', y='Counts', color='Page Name')
            st.altair_chart(c, use_container_width=True)

            p = px.pie(pg_count, values='Counts', names='Page Name')
            st.plotly_chart(p, use_container_width=True)

        with st.expander('Emotion Classifier Metrics'):
            df_emotions = pd.DataFrame(view_all_prediction_details(), columns=['Rawtext', 'Prediction', 'Probability', 'Time_of_Visit'])
            st.dataframe(df_emotions)

            prediction_count = df_emotions['Prediction'].value_counts().rename_axis('Prediction').reset_index(name='Counts')
            pc = alt.Chart(prediction_count).mark_bar().encode(x='Prediction', y='Counts', color='Prediction')
            st.altair_chart(pc, use_container_width=True)
		
if __name__ == '__main__':
	main()