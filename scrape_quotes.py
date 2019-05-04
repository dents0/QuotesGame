import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import DictWriter

BASE_URL = "http://quotes.toscrape.com"


def get_data():
    quotes = []
    page = "/page/1"
    while page:
        print(f"Scraping {BASE_URL}{page}...")
        data = requests.get(f"{BASE_URL}{page}")
        soup = BeautifulSoup(data.text, "lxml")
        quotes_data = soup.find_all(class_="quote")
        for item in quotes_data:
            quotes.append({
                "text": item.find(class_="text").get_text(),
                "author": item.find(class_="author").get_text(),
                "bio": item.find("a")["href"]
            })
        next_btn = soup.find(class_="next")
        page = next_btn.find("a")["href"] if next_btn else None
        sleep(1)
    return quotes


def write_quotes(quotes):
    with open("quotes.csv", "w", encoding="utf-8") as file:
        headers = ["text", "author", "bio"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)


quotes = get_data()
write_quotes(quotes)
