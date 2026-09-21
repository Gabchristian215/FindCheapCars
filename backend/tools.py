import requests
from bs4 import BeautifulSoup
from agents import function_tool

location = input("Enter the location to search for cars: ")
maxYear = int(input("Enter the maximum year of the car: "))
maxPrice = int(input("Enter the maximum price of the car: "))
model = input("Enter the model of the car: ")
make = input("Enter the make of the car: ")

url = f"https://www.craigslist.org/search/area/{location}?auto_make_model={model}%20{make}&cat=cta&max_auto_year={maxYear}&max_price={maxPrice}#search=2~gallery~0"
url2 = "https://www.craigslist.org/search/area/newyork?cat=cta#search=2~gallery~0" # test web page

response = requests.get(url2)
html = response.text

soup = BeautifulSoup(html, "lxml")

print(soup)

results = soup.find_all("li", class_="cl-static-search-result")

for result in results:
    title = result.find("div", class_="title").text
    price = result.find("div", class_="price").text
    location = result.find("div", class_="location").text
    link = result.find("a")["href"]

    if price:
        price = result.find("div", class_="price").text
    else:
        price = "No Price"


    print("Title: ", title.strip())
    print("Price: ", price.strip())
    print("Location: ", location.strip())
    print("Link: ", link.strip())
    print("\n")





