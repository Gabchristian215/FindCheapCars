from fastapi import APIRouter
from agents import Runner
from backend.models.car import CarSearchQuery
from backend.agent import watcher, matcher

router = APIRouter()


@router.post("/search")
async def search_cars(query: CarSearchQuery):
    # Construct a descriptive search prompt from the query parameters
    query_parts = []
    if query.make:
        query_parts.append(f"Make: {query.make}")
    if query.model:
        query_parts.append(f"Model: {query.model}")
    if query.max_price:
        query_parts.append(f"Max Price: ${query.max_price}")
    if query.min_year:
        query_parts.append(f"Min Year: {query.min_year}")
    if query.location:
        query_parts.append(f"Location: {query.location}")

    user_query = ", ".join(query_parts) if query_parts else "cheap cars"

    # 1. Run watcher (scraper) agent
    result = await Runner.run(watcher, user_query)
    listings = result.final_output

    # 2. Run matcher agent to evaluate scraped listings against user request
    choices = await Runner.run(
        matcher,
        f"User Request: {user_query}\n\nListings from scraper:\n{listings}",
    )

    return {
        "preferences": query.model_dump(),
        "choices": choices.final_output,
    }

