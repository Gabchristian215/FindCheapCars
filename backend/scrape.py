import requests
from bs4 import BeautifulSoup




def ScrapeCar(location: str, make: str | None = None, model: str | None = None, max_price: int | None = None, min_year: int | None = None):

    # Filter search to cars and trucks only ("cta" = cars & trucks - all)
    params = {"cat": "cta"}

   # Add max price filter if provided
    if max_price is not None:
        params["max_price"] = int(max_price)
    
    if min_year is not None:
        params["min_auto_year"] = min_year

# Add make/model filter if provided (handles "Honda Civic", just "Toyota", or just "Civic")
    if make or model:
        params["auto_make_model"] = " ".join(
            value for value in [make, model] if value
        )

    url = f"https://www.craigslist.org/search/area/{location}"
    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

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



