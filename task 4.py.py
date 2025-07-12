import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

books = soup.find_all("article", class_="product_pod")

with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])

    for book in books:
        name = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating_class = book.p["class"][1]
        writer.writerow([name, price, rating_class])

print("✅ Product data has been saved to products.csv")

input("\nPress Enter to exit...")
