from scraper import scrape
from summarizer import summarize

url = input("Enter the URL of the article to summarize: ")
title, text = scrape(url)

summary = summarize(title, text)
print(f"Summary of the article titled '{title}':\n{summary}")