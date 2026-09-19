import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool
from openai import AsyncOpenAI

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:2]}")
else:
    print("Google API Key not set")

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

gemini_client = AsyncOpenAI(
    base_url=GEMINI_BASE_URL,
    api_key=google_api_key,
)
gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=gemini_client,
)

# 1. Orchestra Conductor
conductor_agent = Agent(
    name="Orchestra Conductor",
    instructions=(
        "You are the orchestra conductor. Your job is to orchestrate and coordinate "
        "the workflow among the specialized car search agents: Watcher, Matcher, Advisor, "
        "and Notifier. Manage the full pipeline from finding listings, filtering them against "
        "user preferences, scoring and mechanical evaluation, to delivering notifications."
    ),
    model=gemini_model,
)

# 2. Watcher
watcher_agent = Agent(
    name="Watcher",
    instructions=(
        "You are the Watcher. Your job is to find new car listings from Craigslist "
        "or Facebook Marketplace. Strictly search, extract, and collect new vehicle listings "
        "without any conversational personality."
    ),
    model=gemini_model,
)

# 3. Matcher
matcher_agent = Agent(
    name="Matcher",
    instructions=(
        "You are the Matcher. Your job is to filter car listings against user preferences "
        "(such as price, make, model, year, mileage, and location). Strictly evaluate criteria "
        "and filter listings without any conversational personality."
    ),
    model=gemini_model,
)

# 4. Advisor
advisor_agent = Agent(
    name="Advisor",
    instructions=(
        "You are the Advisor, acting as an experienced mechanic dad. Your job is to score each car, "
        "provide detailed reasoning on why this car is recommended or not, and use a RAG implementation "
        "to retrieve vehicle reliability records, common mechanical failure points, and technical specifications. "
        "Provide factual and practical evaluations without any conversational personality."
    ),
    model=gemini_model,
)

# 5. Notifier
notifier_agent = Agent(
    name="Notifier",
    instructions=(
        "You are the Notifier. Your job is to notify users about matched and approved car listings. "
        "Deliver clear, direct, and formatted alerts and summaries to users without any conversational personality."
    ),
    model=gemini_model,
)

# Aliases
orchestra_conductor = conductor_agent
conductor = conductor_agent
watcher = watcher_agent
matcher = matcher_agent
advisor = advisor_agent
notifier = notifier_agent
agent = conductor_agent
