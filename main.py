import streamlit as st
import pickle
import requests
from urllib.parse import urlparse
from Utils.Address_bar_Features import *
from Utils.Domain_Based_Features import *
from Utils.HTML_JS_Based_Features import *
import whois
from urllib.error import URLError

st.set_page_config(
    page_title="URL Feature Extraction and Prediction",
    page_icon="images/favicon/favicon-32x32.png"
)
