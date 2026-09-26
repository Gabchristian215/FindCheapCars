from openai.types.responses import response_format_text_json_schema_config
import requests
from bs4 import BeautifulSoup
from agents import function_tool



@function_tool
def ScrapeCar(location: str, maxYear: int, maxPrice: int, model: str, make: str):
    url = f"https://www.craigslist.org/search/area/{location}?auto_make_model={model}%20{make}&cat=cta&max_auto_year={maxYear}&max_price={maxPrice}#search=2~gallery~0"
   

    response = requests.get(url)
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





#print(ScrapeCar.params_json_schema)
