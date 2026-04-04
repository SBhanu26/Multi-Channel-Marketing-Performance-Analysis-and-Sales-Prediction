import streamlit as st
import pickle
import pandas as pd

# Load model
model=pickle.load(open("C:/Users/bhanu/OneDrive/Desktop/data/knn_model2.pkl", "rb"))
st.title("KNN Prediction App")

# User Inputs
region = st.selectbox("Region", ["East", "West", "North","South","Central"])
channel = st.selectbox("Channel", ["social media","affiliate","influencer","email","tv","search"])
product_category=st.selectbox("Product Category",["Stationery","Storage","Kitchen","Seasonal","General","Lighting"])
customer_segment=st.selectbox("Customer Segment",["Budget","Standard","Premium"])
ad_spend = st.number_input("Ad Spend")
price = st.number_input("Price")
discount_rate = st.number_input("Discount Rate")
market_reach = st.number_input("Market Reach")
impressions = st.number_input("Impressions")

# Create input dataframe
input_df = pd.DataFrame({
    "region": [region],
    "channel": [channel],
    "product_category":[product_category],
    "customer_segment":[customer_segment],
    "ad_spend": [ad_spend],
    "price": [price],
    "discount_rate": [discount_rate],
    "market_reach": [market_reach],
    "impressions": [impressions],


})

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Prediction: {prediction[0]}")