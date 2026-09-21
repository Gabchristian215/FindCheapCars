import requests
from bs4 import BeautifulSoup
from agents import function_tool


@function_tool
def search_craigslist_cars(
    location: str,
    make: str,
    model: str,
    max_year: int,
    max_price: int,
    max_results: int = 20,
) -> list[dict[str, str]]:
    """Search Craigslist for cars matching a user's criteria.

    Args:
        location: Craigslist area slug, such as ``newyork`` or ``sfbay``.
        make: Vehicle manufacturer, such as ``Honda``.
        model: Vehicle model, such as ``Civic``.
        max_year: Latest acceptable model year.
        max_price: Maximum acceptable price in US dollars.
        max_results: Maximum number of listings to return.

    Returns:
        Matching listings with their title, price, location, and URL.
    """
    if max_results < 1:
        return []

    url = f"https://www.craigslist.org/search/area/{location.strip()}"
    response = requests.get(
        url,
        params={
            "auto_make_model": f"{make} {model}".strip(),
            "cat": "cta",
            "max_auto_year": max_year,
            "max_price": max_price,
        },
        headers={"User-Agent": "FindCheapCars/0.1"},
        timeout=15,
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    listings: list[dict[str, str]] = []

    for result in soup.find_all("li", class_="cl-static-search-result"):
        title = result.find("div", class_="title")
        price = result.find("div", class_="price")
        listing_location = result.find("div", class_="location")
        link = result.find("a")

        if title is None or link is None or not link.get("href"):
            continue

        listings.append(
            {
                "title": title.get_text(strip=True),
                "price": price.get_text(strip=True) if price else "No Price",
                "location": (
                    listing_location.get_text(strip=True)
                    if listing_location
                    else "Unknown"
                ),
                "url": str(link["href"]).strip(),
            }
        )

        if len(listings) >= max_results:
            break

    return listings
