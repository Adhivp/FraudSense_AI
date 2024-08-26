import re
import requests
from bs4 import BeautifulSoup

def iframe(response):
    """
    Check for IFrame redirection.
    """
    if response == "":
        return 1
    else:
        if re.findall(r"[|]", response.text):
            return 0
        else:
            return 1

def mouseOver(response):
    """
    Check for status bar customization with onMouseOver.
    """
    if response == "":
        return 1
    else:
        if re.findall(r"onMouseOver", response.text):
            return 1
        else:
            return 0

def rightClick(response):
    """
    Check if right-click is disabled with JavaScript.
    """
    if response == "":
        return 1
    else:
        if re.findall(r"event.button ?== ?2", response.text):
            return 0
        else:
            return 1

def forwarding(response):
    """
    Check the number of URL forwardings.
    """
    if response == "":
        return 1
    else:
        if len(response.history) <= 2:
            return 0
        else:
            return 1
