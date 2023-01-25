'''
This file's contents were taken from the
 Churnometer Walk trough Project 2 and customized for
 this project
'''
import streamlit as st


def predict_sale_price(X_live, features, pipeline):

    # from live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(features)

    # predict
    sale_price_prediction = pipeline.predict(X_live_sale_price)

    return float(sale_price_prediction.round(2))