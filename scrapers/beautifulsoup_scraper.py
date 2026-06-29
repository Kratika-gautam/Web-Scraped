"""
CodeAlpha Internship Project - Task 3: Web Scraping & Data Collection
Author: [Your Name]
Description: Web scraping using BeautifulSoup to collect datasets from public websites
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import csv
import os

# ─────────────────────────────────────────────
# 1. BOOKS DATA SCRAPER (books.toscrape.com)
# ─────────────────────────────────────────────

def scrape_books(pages=5):
    """
    Scrapes book data from books.toscrape.com
    Collects: Title, Price, Rating, Availability
    """
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    books_data = []

    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    print(f"[+] Scraping Books Data from books.toscrape.com ({pages} pages)...")

    for page in range(1, pages + 1):
        url = base_url.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            print(f"  [!] Failed to fetch page {page}")
            continue

        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all("article", class_="product_pod")

        for book in articles:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text.strip().replace("Â", "")
            rating_word = book.find("p", class_="star-rating")["class"][1]
            rating = rating_map.get(rating_word, 0)
            availability = book.find("p", class_="instock availability").text.strip()

            books_data.append({
                "Title": title,
                "Price (£)": float(price.replace("£", "")),
                "Rating (1-5)": rating,
                "Availability": availability
            })

        print(f"  [✓] Page {page} scraped - {len(articles)} books found")
        time.sleep(1)  # Be polite to the server

    df = pd.DataFrame(books_data)
    output_path = "data/books_dataset.csv"
    df.to_csv(output_path, index=False)
    print(f"\n[✓] Books dataset saved! Total records: {len(df)}")
    print(df.head())
    return df


# ─────────────────────────────────────────────
# 2. QUOTES SCRAPER (quotes.toscrape.com)
# ─────────────────────────────────────────────

def scrape_quotes(pages=5):
    """
    Scrapes quotes from quotes.toscrape.com
    Collects: Quote text, Author, Tags
    """
    base_url = "http://quotes.toscrape.com/page/{}/"
    quotes_data = []

    print(f"\n[+] Scraping Quotes Data ({pages} pages)...")

    for page in range(1, pages + 1):
        url = base_url.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            print(f"  [!] Failed to fetch page {page}")
            break

        soup = BeautifulSoup(response.content, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        if not quotes:
            print(f"  [!] No more quotes found at page {page}")
            break

        for quote in quotes:
            text = quote.find("span", class_="text").text.strip().strip('"').strip('"')
            author = quote.find("small", class_="author").text.strip()
            tags = [tag.text for tag in quote.find_all("a", class_="tag")]

            quotes_data.append({
                "Quote": text,
                "Author": author,
                "Tags": ", ".join(tags),
                "Tag Count": len(tags)
            })

        print(f"  [✓] Page {page} scraped - {len(quotes)} quotes found")
        time.sleep(1)

    df = pd.DataFrame(quotes_data)
    output_path = "data/quotes_dataset.csv"
    df.to_csv(output_path, index=False)
    print(f"\n[✓] Quotes dataset saved! Total records: {len(df)}")
    print(df.head())
    return df


# ─────────────────────────────────────────────
# 3. HTML STRUCTURE EXPLORER
# ─────────────────────────────────────────────

def explore_html_structure(url):
    """
    Helper: Explore any webpage HTML structure
    Useful to understand a site before scraping
    """
    print(f"\n[+] Exploring HTML Structure of: {url}")
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.content, "html.parser")

    print(f"\n  📄 Page Title     : {soup.title.text if soup.title else 'N/A'}")
    print(f"  🔗 Total Links    : {len(soup.find_all('a'))}")
    print(f"  🖼️  Total Images   : {len(soup.find_all('img'))}")
    print(f"  📋 Total Tables   : {len(soup.find_all('table'))}")
    print(f"  📦 Total Divs     : {len(soup.find_all('div'))}")

    headings = {f"H{i}": len(soup.find_all(f"h{i}")) for i in range(1, 7)}
    print(f"\n  Headings: {headings}")

    print("\n  Meta Tags:")
    for meta in soup.find_all("meta")[:5]:
        print(f"    {meta}")


# ─────────────────────────────────────────────
# MAIN RUNNER
# ─────────────────────────────────────────────

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    print("=" * 60)
    print("  CodeAlpha Project - Web Scraping & Data Collection")
    print("=" * 60)

    # Run scrapers
    books_df = scrape_books(pages=5)
    quotes_df = scrape_quotes(pages=5)

    # Explore HTML structure
    explore_html_structure("http://books.toscrape.com")

    print("\n" + "=" * 60)
    print("  ✅ All datasets collected successfully!")
    print("  📁 Check the /data folder for CSV files")
    print("=" * 60)
