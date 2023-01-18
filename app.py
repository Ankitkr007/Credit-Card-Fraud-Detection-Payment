import requests
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn





pickle_in=open("C:/Users/hp/Downloads/model5.pkl","rb")
model5=pickle.load(pickle_in)


def predict_fraud_payment_detection(step,type,amount,oldbalanceOrig,newbalanceOrig,oldbalanceDest,newbalanceDest):
    prediction=model5.predict([[step,type,amount,oldbalanceOrig,newbalanceOrig,oldbalanceDest,newbalanceDest]])
    print(prediction)
    return prediction


def main():
    st.title("Credit Card Payment Fraud Detector")
    html_temp="""
    <div style="background-color:tomato;padding:10px>
    <h2 style='color:white;text-align:center;">Streamlit Credit Card Fraud Detector ML App </h2>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    step = st.text_input("step", "Type Here")
    type = st.text_input("type", "Type Here")
    amount = st.text_input("amount", "Type Here")
    oldbalanceOrig = st.text_input("oldbalanceOrig", "Type Here")
    newbalanceOrig = st.text_input("newbalanceOrig", "Type Here")
    oldbalanceDest = st.text_input("oldbalanceDest", "Type Here")
    newbalanceDest = st.text_input("newbalanceDest", "Type Here")

    result = ""
    if st.button("Predict"):
        result =predict_fraud_payment_detection(step,type,amount,oldbalanceOrig,newbalanceOrig,oldbalanceDest,newbalanceDest)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")


if __name__ == '__main__':
    main()







