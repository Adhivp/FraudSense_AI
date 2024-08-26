
from urllib.parse import urlparse
import ipaddress
import re

# Define URL shortening services regex pattern
shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"

def getDomain(url):
    """
    Extract the domain from the URL. 
    """
    domain = urlparse(url).netloc
    if re.match(r"^www\.", domain):
        domain = domain.replace("www.", "")
    return domain

def havingIP(url):
    """
    Check if the URL contains an IP address instead of a domain name.
    """
    try:
        ipaddress.ip_address(url)
        return 1
    except ValueError:
        return 0

def haveAtSign(url):
    """
    Check for the presence of '@' in the URL.
    """
    return 1 if "@" in url else 0

def getLength(url):
    """
    Return 1 if the length of the URL is greater than or equal to 54 characters, otherwise 0.
    """
    return 1 if len(url) >= 54 else 0

def getDepth(url):
    """
    Calculate the depth of the URL based on the number of '/' in the path.
    """
    path = urlparse(url).path.split('/')
    depth = sum(len(part) != 0 for part in path)
    return depth

def redirection(url):
    """
    Check for the presence of "//" in the URL path, excluding the protocol part.
    """
    pos = url.rfind('//')
    return 1 if pos > 6 else 0

def httpDomain(url):
    """
    Check if 'https' is present in the domain part of the URL.
    """
    domain = urlparse(url).netloc
    return 1 if 'https' in domain else 0

def tinyURL(url):
    """
    Check if the URL uses a known shortening service.
    """
    return 1 if re.search(shortening_services, url) else 0

def prefixSuffix(url):
    """
    Check for the presence of '-' in the domain part of the URL.
    """
    return 1 if '-' in urlparse(url).netloc else 0
