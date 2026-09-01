import requests
from bs4 import BeautifulSoup

def scrape(url):
    """
    Scrapes the content of the given URL and returns the HTML content.

    Args:
        url (str): The URL to scrape.
    """
    print(f"Scraping URL: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.text if soup.title else "No title found"
        text = soup.get_text(" ", strip=True)

        return title, text
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while scraping {url}: {e}")
        return None
