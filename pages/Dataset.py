import streamlit as st
import pandas as pd

st.title("Dataset Descriptions")

st.subheader("1. Legitimate URLs Dataset (legitimate.csv)")
st.write("""
This file contains the extracted features of 5,000 legitimate URLs. These URLs are randomly selected from a larger dataset of benign URLs. The dataset provides a robust set of features that help in identifying legitimate web pages.
""")

st.subheader("2. Phishing URLs Dataset (phishing.csv)")
st.write("""
This file contains the extracted features of 5,000 phishing URLs. These URLs are randomly selected from a dataset provided by PhishTank, a well-known open-source service that tracks phishing activities. The dataset is designed to help in detecting and analyzing phishing attempts.
""")

st.subheader("3. Combined URLs Dataset (Combined_data.csv)")
st.write("""
This file is a combination of the legitimate and phishing datasets, containing a total of 10,000 URLs. It includes extracted features from both legitimate and phishing URLs, providing a comprehensive dataset for training and testing machine learning models.
""")

dataset_dir = "Dataset/"
legitimate_df = pd.read_csv(dataset_dir + "legitimate.csv")
phishing_df = pd.read_csv(dataset_dir + "phishing.csv")
urldata_df = pd.read_csv(dataset_dir + "Combined_data.csv")


st.subheader("legitimate.csv")
st.dataframe(legitimate_df)

st.subheader("phishing.csv")
st.dataframe(phishing_df)

st.subheader("Combined_data.csv")
st.dataframe(urldata_df)