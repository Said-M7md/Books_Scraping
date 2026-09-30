import csv
import re
import requests
from bs4 import BeautifulSoup

# Map word ratings to numerical values
RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

base_url = "https://books.toscrape.com/catalogue/page-{}.html"
books_data = []

# Loop through pages 1 to 5 (20 books per page = 100 books total)
for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    articles = soup.find_all("article", class_="product_pod")
    
    for article in articles:
        # Extract title
        title = article.h3.a["title"]
        
        # Extract price as a float (e.g., "£51.77" -> 51.77)
        price_raw = article.find("p", class_="price_color").text
        price = float(re.sub(r"[^\d.]", "", price_raw))
        
        # Extract rating as integer (1-5)
        rating_class = article.find("p", class_="star-rating")["class"]
        rating_word = [c for c in rating_class if c != "star-rating"][0]
        rating = RATING_MAP.get(rating_word, None)
        
        # Extract in_stock as boolean (True/False)
        availability = article.find("p", class_="instock availability").text.strip()
        in_stock = "In stock" in availability
        
        books_data.append({
            "title": title,
            "price": price,
            "rating": rating,
            "in_stock": in_stock
        })

# Write collected data to CSV
with open("books.csv", mode="w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["title", "price", "rating", "in_stock"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(books_data)

print(f"Successfully saved {len(books_data)} books to books.csv!")