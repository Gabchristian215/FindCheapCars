import requests
from bs4 import BeautifulSoup
from agents import function_tool



@function_tool
def ScrapeCar(location: str, price: int):
    """Scrape Craigslist for car listings based on location and price.
    Args:
        location: The location to search for car listings.
        price: The maximum price to search for car listings.
    Returns:
        A list of car listings.
    """
    
    url = f"https://www.craigslist.org/search/area/{location}?cat=cta&max_price={price}#search=2~gallery~0"

    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, "lxml")

    results = soup.find_all("li", class_="cl-static-search-result")
    cars = []

    for result in results:
        title_elem = result.find("div", class_="title")
        price_elem = result.find("div", class_="price")
        location_elem = result.find("div", class_="location")
        link_elem = result.find("a")

        cars.append({
            "title": title_elem.text.strip() if title_elem else "No Title",
            "price": price_elem.text.strip() if price_elem else "No Price",
            "location": location_elem.text.strip() if location_elem else "No Location",
            "link": link_elem["href"].strip() if link_elem and link_elem.has_attr("href") else "",
        })

    return cars

"""
def print_car_results(cars: list[dict]):
    print(f"\n{'=' * 70}")
    print(f" Found {len(cars)} Listings")
    print(f"{'=' * 70}\n")

    for idx, car in enumerate(cars, 1):
        print(f"[{idx:>2}] {car['title']}")
        print(f"     Price:    {car['price']}")
        print(f"     Location: {car['location']}")
        print(f"     Link:     {car['link']}")
        print(f"{'-' * 70}")


if __name__ == "__main__":
    listings = ScrapeCar("newyork", 2000)
    print_car_results(listings)
"""

# print(ScrapeCar.params_json_schema)
