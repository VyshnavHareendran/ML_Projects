import streamlit as st
import pandas as pd
import joblib
import lightgbm as lgb
from geopy.distance import geodesic
import base64

def set_bg_and_style(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        /* Background image */
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            font-family: 'Segoe UI', sans-serif;
        }}

        /* Glass effect container */
        .block-container {{
            background-color: rgba(0, 0, 0, 0.55);
            padding: 3rem 2rem;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
        }}

        h1 {{
            color: #ffffff;
            text-align: center;
            font-weight: bold;
        }}

        .stTextInput > div > div > input {{
            padding: 0.8rem !important;
            vertical-align: middle !important;
            line-height: normal !important;
            height: 40px !important;
        }},
        .stNumberInput > div > div > input,
        .stSelectbox > div > div,
        .stSlider > div {{
            background-color: #2c2c2c !important;
            border-radius: 10px;
            padding: 10px;
            height: 60px;
            line-height: -10px;  /* Vertically center the text */
            vertical-align: middle;
            color: white;
            font-size: 1rem;
        }}

        
        .stButton > button{{
            display: flex;
            justify-content: center;
        }}

        .stButton > button {{
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 0.6rem 1.2rem;
            font-size: 1rem;
            border-radius: 8px;
            transition: 0.3s;
            cursor: pointer;
        }}
        .stButton > button:hover {{
            background-color: #1c1c1c;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_and_style("assets/background1.jpeg") 




model = joblib.load("fraud_detection_model.jb")
encoder = joblib.load("label_encoder.jb")

def haversine(lat1,lon1,lat2,lon2):
    return geodesic((lat1,lon1),(lat2,lon2)).km

st.title("Vyshnav's Credit-Card Fraud Detection System")
st.markdown(
    "<h4 style='text-align: center; color: white;'>Enter the transaction details below</h4>",
    unsafe_allow_html=True
)
st.caption("Model: LightGBM | Trained on: credit_card_dataset_v1 | Version: 1.0")

merchant =  st.text_input("Merchant Name")
category =  st.text_input("Category")
amt = st.number_input("Transaction Amount",min_value=0.0,format="%.2f")
lat = st.number_input("Latitude",format="%.6f")
long = st.number_input("Longitude",format="%.6f")
merch_lat = st.number_input("Merchant Latitude",format="%.6f")
merch_long = st.number_input("Merchant Longitude",format="%.6f")
hour = st.slider("Transaction Hour",0,23,12)
day = st.slider("Transaction Day",1,21,15)
month = st.slider("Transaction Month",1,12,6)
gender = st.selectbox("Gender", ["Male", "Female","Others"])
cc_num = st.text_input("Credit Card Number")
distance = haversine(lat,long,merch_lat,merch_long)

if st.button("Check For Fraud"):
    if merchant and category and cc_num:
        try:
            distance = haversine(lat, long, merch_lat, merch_long)
        except ValueError as e:
            st.error(f"Invalid coordinates: {e}")
            st.stop()

        input_data = pd.DataFrame([[merchant,category,amt,distance,hour,day,month,gender,cc_num]],
                                  columns = ['merchant','category','amt','distance','hour','day','month','gender','cc_num'])
        categorical_col = ['merchant','category','gender']
        for col in categorical_col:
            try:
                input_data[col]=encoder[col].transform(input_data[col])
            except ValueError:
                input_data[col]=-1

        input_data['cc_num'] = input_data['cc_num'].apply(lambda x:hash(x) % (10**2))

        st.markdown("### Transaction Summary")
        st.dataframe(input_data)

        prediction = model.predict(input_data)[0]
        result = "Fradulent Transaction" if prediction == 1 else "Legitimate Transaction"
        st.subheader(f"Prediction: {result}")
    else:
        st.error("Please Fill all requires fields")

if st.button("Reset"):
    st.warning("Please manually refresh the page (Ctrl+R)")