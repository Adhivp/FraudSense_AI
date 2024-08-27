import re
from bs4 import BeautifulSoup
import whois
import urllib
import urllib.request
from datetime import datetime, timezone
import pandas as pd
import json
import socket
from fuzzywuzzy import fuzz

def get_dns_record(domain):
    """
    Check if DNS record is available for the domain.
    """
    try:
        whois_info = whois.whois(domain)
        if whois_info.domain_name:
            return 0  
        else:
            return 1  
    except Exception:
        return 1  

def web_traffic(url, csv_file='/Users/adhivp/Desktop/FraudSense AI/Utils/Datasets/top100K_domains.csv', similarity_threshold=80):
    """
    Check if the domain is in the top 100k domains CSV file or is similar to any in the list.
    
    :param url: The URL of the domain to check.
    :param csv_file: The CSV file containing the list of top domains.
    :param similarity_threshold: The similarity threshold to consider a match (0-100).
    :return: 0 if the domain is in the top 100k or similar, otherwise 1.
    """
    try:
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc
        
        top_domains = pd.read_csv(csv_file, header=None)[0].tolist()
        
        if domain in top_domains:
            return 0
        
        for top_domain in top_domains:
            similarity = fuzz.ratio(domain, top_domain)
            if similarity >= similarity_threshold:
                return 0
        
        return 1
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

def domain_age(domain_info):
    """
    Calculate the age of the domain.
    
    :param domain_name: The domain name as a string.
    :return: 0 if the domain age is >= 12 months, otherwise 1.
    """
    try:
        creation_date = domain_info.creation_date
        expiration_date = domain_info.expiration_date
        
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        
        if isinstance(creation_date, str):
            creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
        if isinstance(expiration_date, str):
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        
        if creation_date is None or expiration_date is None:
            return 1
        
        age_of_domain = abs((expiration_date - creation_date).days)
        return 0 if (age_of_domain / 30) >= 12 else 1
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return 1

def domain_end(domain_info):
    """
    Calculate the remaining time until the domain expires.
    Returns 1 if the domain expires within 6 months, otherwise returns 0.
    """
    expiration_date = domain_info.expiration_date

    if isinstance(expiration_date, list):
        expiration_date = [date.astimezone(timezone.utc).replace(tzinfo=None) if date.tzinfo else date for date in expiration_date]
        expiration_date = max(expiration_date)
    
    if isinstance(expiration_date, str):
        try:
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        except ValueError:
            return 1
    
    if expiration_date is None:
        return 1
    
    today = datetime.now()
    end_period = abs((expiration_date - today).days)
    
    return 1 if (end_period / 30) <= 6 else 0
