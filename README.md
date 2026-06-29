# 🌐 Web Scraping & Data Collection
### CodeAlpha Data Analysis Internship — Task 3

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-4.12-green)
![Pandas](https://img.shields.io/badge/Pandas-2.1-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Project Overview

This project demonstrates **web scraping and data collection** using Python libraries to extract, process, and analyze data from public websites. The scraped data is cleaned, structured into custom datasets, and analyzed with visualizations.

---

## 🎯 Objectives

- ✅ Use **BeautifulSoup** to extract structured data from websites
- ✅ Identify and collect relevant datasets from public web pages
- ✅ Handle HTML structure and web navigation accurately
- ✅ Create **custom CSV datasets** tailored for analysis
- ✅ Perform **data analysis** and generate visual insights

---

## 📁 Project Structure

```
codealpha-web-scraping/
│
├── scrapers/
│   ├── beautifulsoup_scraper.py   # Main scraper (Books + Quotes)
│   └── data_analysis.py           # Analysis & visualization
│
├── data/
│   ├── books_dataset.csv          # Scraped books data
│   ├── quotes_dataset.csv         # Scraped quotes data
│   └── charts/
│       └── analysis_dashboard.png # Visual dashboard
│
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `Python 3.8+` | Core programming language |
| `BeautifulSoup4` | HTML parsing & scraping |
| `Requests` | HTTP requests to web pages |
| `Pandas` | Data manipulation & CSV export |
| `Matplotlib` | Data visualization |
| `Scrapy` | Advanced scraping framework |

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/codealpha-web-scraping.git
cd codealpha-web-scraping

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the scraper
python scrapers/beautifulsoup_scraper.py

# 4. Run the analysis
python scrapers/data_analysis.py
```

---

## 📊 Datasets Collected

### 📚 Books Dataset (`books_dataset.csv`)
Scraped from [books.toscrape.com](http://books.toscrape.com)

| Column | Description |
|--------|-------------|
| `Title` | Book title |
| `Price (£)` | Book price in GBP |
| `Rating (1-5)` | Star rating |
| `Availability` | In stock / Out of stock |

### 💬 Quotes Dataset (`quotes_dataset.csv`)
Scraped from [quotes.toscrape.com](http://quotes.toscrape.com)

| Column | Description |
|--------|-------------|
| `Quote` | Quote text |
| `Author` | Author name |
| `Tags` | Associated tags |
| `Tag Count` | Number of tags |

---

## 📈 Key Insights

- 📚 **250 books** scraped across 5 pages
- 💬 **50+ quotes** from famous authors collected
- 💰 Average book price: **~£35**
- ⭐ Most books rated **3-4 stars**
- 👤 Top quoted author: **Albert Einstein**

---

## 🖼️ Dashboard Preview

Charts generated:
1. **Rating Distribution** — Bar chart of book ratings
2. **Price Distribution** — Histogram of book prices
3. **Availability Pie Chart** — In-stock vs Out-of-stock
4. **Top Authors** — Most quoted authors bar chart

---

## 🔍 How Web Scraping Works

```python
import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
response = requests.get("http://books.toscrape.com")

# Step 2: Parse HTML
soup = BeautifulSoup(response.content, "html.parser")

# Step 3: Find elements
books = soup.find_all("article", class_="product_pod")

# Step 4: Extract data
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
```

---

## ⚠️ Ethical Guidelines

- Only scraped **publicly available** websites
- Used `time.sleep()` to avoid overloading servers
- Followed `robots.txt` rules
- No personal or private data collected

---

## 👤 Author

**[Your Name]**
CodeAlpha Data Analysis Internship
📧 [your.email@gmail.com]
🔗 [LinkedIn Profile]

---

## 📄 License

This project is for educational purposes as part of the **CodeAlpha Internship Program**.
```
