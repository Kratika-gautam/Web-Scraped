"""
CodeAlpha Internship Project - Data Analysis on Scraped Datasets
Author: [Your Name]
Description: Analyze and visualize the scraped web data
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import os

os.makedirs("data", exist_ok=True)
os.makedirs("data/charts", exist_ok=True)

# ─────────────────────────────────────────────
# GENERATE SAMPLE DATA (if CSVs not yet scraped)
# ─────────────────────────────────────────────

import random

def generate_sample_books():
    titles = [f"Book Title {i}" for i in range(1, 51)]
    prices = [round(random.uniform(10, 60), 2) for _ in range(50)]
    ratings = [random.randint(1, 5) for _ in range(50)]
    availability = random.choices(["In stock", "Out of stock"], weights=[80, 20], k=50)
    df = pd.DataFrame({"Title": titles, "Price (£)": prices, "Rating (1-5)": ratings, "Availability": availability})
    df.to_csv("data/books_dataset.csv", index=False)
    return df

def generate_sample_quotes():
    authors = ["Einstein", "Twain", "Aristotle", "Gandhi", "Tesla", "Lincoln", "Newton"]
    tag_pool = ["life", "wisdom", "love", "science", "truth", "inspiration", "change"]
    data = []
    for i in range(50):
        data.append({
            "Quote": f"Sample quote number {i+1} about life and wisdom.",
            "Author": random.choice(authors),
            "Tags": ", ".join(random.sample(tag_pool, k=random.randint(1, 4))),
            "Tag Count": random.randint(1, 4)
        })
    df = pd.DataFrame(data)
    df.to_csv("data/quotes_dataset.csv", index=False)
    return df

# Load or generate data
try:
    books_df = pd.read_csv("data/books_dataset.csv")
    print("[✓] Loaded books_dataset.csv")
except FileNotFoundError:
    print("[!] books_dataset.csv not found - generating sample data...")
    books_df = generate_sample_books()

try:
    quotes_df = pd.read_csv("data/quotes_dataset.csv")
    print("[✓] Loaded quotes_dataset.csv")
except FileNotFoundError:
    print("[!] quotes_dataset.csv not found - generating sample data...")
    quotes_df = generate_sample_quotes()


# ─────────────────────────────────────────────
# ANALYSIS 1: BOOKS DATASET
# ─────────────────────────────────────────────

print("\n" + "="*50)
print("📚 BOOKS DATASET ANALYSIS")
print("="*50)
print(f"Total Books     : {len(books_df)}")
print(f"Average Price   : £{books_df['Price (£)'].mean():.2f}")
print(f"Highest Price   : £{books_df['Price (£)'].max():.2f}")
print(f"Lowest Price    : £{books_df['Price (£)'].min():.2f}")
print(f"Avg Rating      : {books_df['Rating (1-5)'].mean():.2f} / 5")
print(f"\nAvailability Breakdown:\n{books_df['Availability'].value_counts()}")
print(f"\nRating Distribution:\n{books_df['Rating (1-5)'].value_counts().sort_index()}")

# Chart 1: Rating Distribution
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("CodeAlpha Project - Web Scraped Data Analysis", fontsize=16, fontweight='bold')

rating_counts = books_df['Rating (1-5)'].value_counts().sort_index()
axes[0, 0].bar(rating_counts.index, rating_counts.values, color=['#ff6b6b','#ffa500','#ffd700','#90ee90','#4CAF50'])
axes[0, 0].set_title("Books - Rating Distribution")
axes[0, 0].set_xlabel("Rating (Stars)")
axes[0, 0].set_ylabel("Number of Books")
for i, v in enumerate(rating_counts.values):
    axes[0, 0].text(rating_counts.index[i], v + 0.3, str(v), ha='center', fontweight='bold')

# Chart 2: Price Distribution
axes[0, 1].hist(books_df['Price (£)'], bins=15, color='#667eea', edgecolor='white')
axes[0, 1].set_title("Books - Price Distribution")
axes[0, 1].set_xlabel("Price (£)")
axes[0, 1].set_ylabel("Frequency")
axes[0, 1].axvline(books_df['Price (£)'].mean(), color='red', linestyle='--', label=f"Mean: £{books_df['Price (£)'].mean():.2f}")
axes[0, 1].legend()

# Chart 3: Availability Pie
avail_counts = books_df['Availability'].value_counts()
axes[1, 0].pie(avail_counts.values, labels=avail_counts.index, autopct='%1.1f%%',
               colors=['#4CAF50', '#ff6b6b'], startangle=90)
axes[1, 0].set_title("Books - Availability")

# ─────────────────────────────────────────────
# ANALYSIS 2: QUOTES DATASET
# ─────────────────────────────────────────────

print("\n" + "="*50)
print("💬 QUOTES DATASET ANALYSIS")
print("="*50)
print(f"Total Quotes    : {len(quotes_df)}")
print(f"Unique Authors  : {quotes_df['Author'].nunique()}")
print(f"\nTop 5 Authors:\n{quotes_df['Author'].value_counts().head()}")
print(f"\nAvg Tags per Quote: {quotes_df['Tag Count'].mean():.2f}")

# Chart 4: Top Authors
top_authors = quotes_df['Author'].value_counts().head(8)
axes[1, 1].barh(top_authors.index[::-1], top_authors.values[::-1], color='#764ba2')
axes[1, 1].set_title("Quotes - Top Authors")
axes[1, 1].set_xlabel("Number of Quotes")

plt.tight_layout()
chart_path = "data/charts/analysis_dashboard.png"
plt.savefig(chart_path, dpi=150, bbox_inches='tight')
print(f"\n[✓] Dashboard chart saved to: {chart_path}")

# ─────────────────────────────────────────────
# SUMMARY REPORT
# ─────────────────────────────────────────────

print("\n" + "="*50)
print("📊 SUMMARY REPORT")
print("="*50)
print(f"  Books Scraped     : {len(books_df)}")
print(f"  Quotes Scraped    : {len(quotes_df)}")
print(f"  Unique Authors    : {quotes_df['Author'].nunique()}")
print(f"  Avg Book Price    : £{books_df['Price (£)'].mean():.2f}")
print(f"  Avg Book Rating   : {books_df['Rating (1-5)'].mean():.1f}/5")
print(f"  Charts Generated  : 1 dashboard (4 charts)")
print(f"  Output Folder     : /data/")
print("\n✅ Analysis complete!")
