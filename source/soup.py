import requests
from bs4 import BeautifulSoup

def return_soup(url) -> BeautifulSoup:
    """Sends a get request to provided website and returns a BeautifulSoup object for that.

    Args:
        url (string): URL of the site.

    Returns:
        BeautifulSoup: BeautifulSoup class created with the response and parsed wiht html parser.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
