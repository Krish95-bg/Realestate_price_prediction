import streamlit as st
import numpy as np
import joblib

scaler  = joblib.load("/Users/krishna/DSuser/projects/scaler.pkl")

model = joblib.load("/Users/krishna/DSuser/projects/model.pkl")


st.title("Real estate price prediction app")

bed = st.number_input("enter the number of the bedrooms",value=2,step=1)
bath = st.number_input("enter the number of the bathrooms",value=1,step=1)
size = st.number_input("enter the number of the size",value=1000,step=50)


x = [bed,bath,size]

st.divider()

predictbutton = st.button("Predict!")

st.divider()

if predictbutton:
    st.balloons()
    x1 = np.array(x)
    x_array = scaler.transform([x1])
    
    prediction = model.predict(x_array)[0]
    st.write(f"The prediction is{prediction:.2f}")
    
    
    
else:
    "Please use the button for prediction"

