import streamlit as st
import pickle

# Load your pickle file (ensure this file is uploaded to the same directory or a location accessible by your app)
def load_pickle():
    with open('random_forest_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Function to interact with the model
def predict(input_data):
    model = load_pickle()
    prediction = model.predict(input_data)  # Replace this with actual prediction code
    return prediction

# Streamlit interface
st.title("Pickle Model Interaction")
user_input = st.text_input("Enter your input:", "Default input")

if st.button('Predict'):
    result = predict(user_input)
    st.write(f"Prediction: {result}")
