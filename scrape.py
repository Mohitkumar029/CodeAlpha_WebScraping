import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

all_books = []

for page in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]
        stock = book.find("p", class_="instock").text.strip()

        all_books.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": stock
        })

    print("Page", page, "done")
    time.sleep(0.5)

df = pd.DataFrame(all_books)
df.to_csv("books_raw.csv", index=False)
print(df.shape)
print(df.head())