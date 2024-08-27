import streamlit as st
import joblib
import requests
from urllib.parse import urlparse
from Utils.Address_bar_Features import *
from Utils.Domain_Based_Features import *
from Utils.HTML_JS_Based_Features import *
import whois
from urllib.error import URLError
import time

st.set_page_config(
    page_title="URL Feature Extraction and Prediction",
    page_icon="images/favicon/favicon-32x32.png"
)

# Splash Screen
st.image("images/FraudSense_Logo.jpeg", width=400)
st.markdown("<p style='text-align: center;'>Securing your web experience</p>", unsafe_allow_html=True)
time.sleep(3)


# Load models
with open('Trained_models/XGBoost.pkl', 'rb') as xgboost_file:
    xgboost_model = joblib.load(xgboost_file)

with open('Trained_models/MLP.pkl', 'rb') as mlp_file:
    mlp_model = joblib.load(mlp_file)

def extract_features(url):
    features = []
    
    try:
        with st.spinner("Extracting Address Bar-Based Features..."):
            def display_feature(label, value):
                color = "red" if value == 1 else "green"
                symbol = "✗" if value == 1 else "✓"
                st.write(f"{label}: <span style='color:{color}'>{symbol}</span>", unsafe_allow_html=True)

            display_feature("Having IP", havingIP(url))
            display_feature("Having '@'", haveAtSign(url))
            display_feature("URL Length", getLength(url))
            display_feature("URL Depth", getDepth(url))
            display_feature("Redirection '//'", redirection(url))
            display_feature("HTTP in Domain", httpDomain(url))
            display_feature("Using Tiny URL", tinyURL(url))
            display_feature("Prefix/Suffix '-'", prefixSuffix(url))
            
            features.extend([
                havingIP(url),
                haveAtSign(url),
                getLength(url),
                getDepth(url),
                redirection(url),
                httpDomain(url),
                tinyURL(url),
                prefixSuffix(url)
            ])

        with st.spinner("Extracting Domain-Based Features..."):
            domain = getDomain(url)
            domain_info = whois.whois(domain)
            
            display_feature("DNS Record Available", get_dns_record(domain))
            display_feature("Web Traffic Rank", web_traffic(url))
            display_feature("Domain Age", domain_age(domain_info))
            display_feature("Domain Expiry", domain_end(domain_info))
            
            features.extend([
                get_dns_record(domain),
                web_traffic(url),
                domain_age(domain_info),
                domain_end(domain_info)
            ])

        with st.spinner("Extracting HTML/JS-Based Features..."):
            response = requests.get(url)
            
            display_feature("Using IFrame", iframe(response))
            display_feature("OnMouseOver Event", mouseOver(response))
            display_feature("Right-Click Disabled", rightClick(response))
            display_feature("URL Forwarding", forwarding(response))
            
            features.extend([
                iframe(response),
                mouseOver(response),
                rightClick(response),
                forwarding(response)
            ])
    
    except URLError as e:
        st.error(f"Failed to retrieve URL data: {e.reason}")
        return None

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

    return features

st.title("URL Feature Extraction and Prediction")

model_option = st.selectbox("Choose Model", ["XGBoost", "MLP"])

url = st.text_input("Enter URL")

if st.button("Predict"):
    features = extract_features(url)
    
    if features:
        model = xgboost_model if model_option == "XGBoost" else mlp_model
        
        with st.spinner(f"Predicting with {model_option} model..."):
            probabilities = model.predict_proba([features])[0]
            # Probabilities for each class (assuming binary classification with 0 as good and 1 as bad)
            prob_good = probabilities[1]  # Probability of class 0 (good)
            prob_bad = probabilities[0]   # Probability of class 1 (bad)
            
            st.write(f"Probability of being Good: {prob_good * 100:.2f}%")
            st.write(f"Probability of being Bad: {prob_bad * 100:.2f}%")
            prediction = model.predict([features])[0]
            print(prediction)
            if prediction == 1:
                st.success("Prediction: Good")
            else:
                st.error("Prediction: Bad")
    else:
        st.error("Failed to extract features. Please check the URL and try again.")
