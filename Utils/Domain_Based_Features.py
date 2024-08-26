# Domain_based_features.py

import re
from bs4 import BeautifulSoup
import whois
import urllib
import urllib.request
from datetime import datetime

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

def web_traffic(url):
    """
    Determine the web traffic rank using Alexa. 
    """
    try:
        url = urllib.parse.quote(url)
        rank = BeautifulSoup(urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find(
            "REACH")['RANK']
        rank = int(rank)
    except (TypeError, AttributeError, ValueError):
        return 1  
    
    return 1 if rank < 100000 else 0

def domain_age(domain_name):
    """
    Calculate the age of the domain. 
    """
    creation_date = domain_name.creation_date
    expiration_date = domain_name.expiration_date
    
    if (isinstance(creation_date, str) or isinstance(expiration_date, str)):
        try:
            creation_date = datetime.strptime(creation_date, '%Y-%m-%d')
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        except ValueError:
            return 1  
    
    if (expiration_date is None) or (creation_date is None):
        return 1 
    elif isinstance(expiration_date, list) or isinstance(creation_date, list):
        return 1  
    else:
        age_of_domain = abs((expiration_date - creation_date).days)
        return 1 if (age_of_domain / 30) >= 12 else 0

def domain_end(domain_name):
    """
    Calculate the remaining time until the domain expires. 
    """
    expiration_date = domain_name.expiration_date
    
    if isinstance(expiration_date, str):
        try:
            expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        except ValueError:
            return 1
    
    if expiration_date is None:
        return 1
    elif isinstance(expiration_date, list):
        return 1  
    else:
        today = datetime.now()
        end_period = abs((expiration_date - today).days)
        return 0 if (end_period / 30) <= 6 else 1
