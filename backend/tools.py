import requests
from bs4 import BeautifulSoup
from agents import function_tool


response = requests.get("https://www.craigslist.org/search/area/newyork?cat=cta#search=2~gallery~0")
print(response.text)
