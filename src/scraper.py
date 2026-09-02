import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException

def scrape_with_requests(url):
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
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(10)

    try:
        try:
            driver.get(url)
        except TimeoutException:
            print(f"Timed out loading {url}, using whatever content loaded so far")

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        title = soup.title.text if soup.title else "No title found"
        text = soup.get_text(" ", strip=True)

        return title, text

    finally:
        driver.quit() # Quit the driver after scraping to free up resources


def has_useful_content(text):
    return len(text.split()) > 100  

def scrape(url):
    try:
        title, text = scrape_with_requests(url)

        if has_useful_content(text):
            print("Using requests as scraping method")
            return title, text
    
    except requests.RequestException:
        pass

    # fall back to selenium
    print("use selenium as the scraping strategy")
    return scrape_with_selenium(url)