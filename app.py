import streamlit as st
import joblib
import pandas as pd
import pickle

# Load the pre-trained RandomForest model
rf_classifier = joblib.load('random_forest_model.pkl')

# Streamlit app interface for user inputs
st.title("Wildlife Species Prediction")

# Input fields for the features
month = st.number_input("Month", min_value=1, max_value=12)
day = st.number_input("Day", min_value=1, max_value=31)
hour = st.number_input("Hour", min_value=0, max_value=23)
site_name_code = st.number_input("Site Name Code", min_value=0, max_value=37)

# Prepare the input for the model
input_data = {
    'Month': [month],
    'Day': [day],
    'Hour': [hour],
    'Site_Name_codes': [site_name_code]
}
input_df = pd.DataFrame(input_data)

# Make a prediction when the button is pressed
if st.button('Predict'):
    predicted_species = rf_classifier.predict(input_df)
    st.write(f"Predicted Species: {predicted_species[0]}")
