"""
Books to Scrape - Web Scraper
Scrapes book data (title, price, rating, availability, category)
from https://books.toscrape.com and exports it to a CSV file
that can be loaded into Power BI (or any BI tool) for analysis.

Usage:
    python books_scraper.py

Requirements:
    pip install requests beautifulsoup4 pandas
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://books.toscrape.com/"
CATALOGUE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}


def get_soup(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def scrape_all_books():
    all_books = []
    page = 1

    while True:
        url = CATALOGUE_URL.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            # No more pages left
            break

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.select("article.product_pod")

        if not books:
            break

        for book in books:
            title = book.h3.a["title"]

            price_text = book.select_one(".price_color").text
            price = float(price_text.replace("£", "").strip())

            availability = book.select_one(".availability").text.strip()

            rating_class = book.select_one("p.star-rating")["class"]
            rating_word = [c for c in rating_class if c != "star-rating"][0]
            rating = RATING_MAP.get(rating_word, None)

            all_books.append({
                "title": title,
                "price_gbp": price,
                "availability": availability,
                "rating": rating,
                "page": page,
            })

        print(f"Scraped page {page} ({len(books)} books)")
        page += 1
        time.sleep(0.5)  # be polite to the server

    return all_books


def main():
    books = scrape_all_books()
    df = pd.DataFrame(books)
    df.to_csv("books_data.csv", index=False)
    print(f"\nDone! {len(df)} books saved to books_data.csv")


if __name__ == "__main__":
    main()
