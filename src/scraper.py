import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def scrape(url):
    """
    Scrapes the content of the given URL ( static page ) and returns the HTML content.

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


def scrape_with_selenium(url):
    """
    Scrapes the content of web pages which makes use of javascript to load the content, it waits 
    for the content to be available before fetching

    Args:
        url (string): The url of the web page to scrape
    """
    
    print(f"Scraping URL: {url}")

    driver = webdriver.Chrome()

    try:

        driver.get(url)
        driver.implicitly_wait(10)

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        title = soup.title.text if soup.title else "No title found"
        text = soup.get_text(" ", strip=True)

        return title, text

    finally:
        driver.quit() # Quit the driver after scraping to free up resources