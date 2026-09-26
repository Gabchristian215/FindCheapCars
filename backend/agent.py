import asyncio
from agents import result
import os

from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, Runner, trace
from openai import AsyncOpenAI
from tools import ScrapeCar
from instructions.watcher import watcher_instruction
from instructions.matcher import matcher_instruction
from instructions.advisor import advisor_instruction
from instructions.notifier import notifier_instruction
from instructions.conductor import conductor_instruction

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
    model="gemini-3.5-flash",
    openai_client=gemini_client,
)

# 1. Watcher
watcher_agent = Agent(
    name="Watcher",
    instructions=watcher_instruction,
    model=gemini_model,
    tools=[ScrapeCar]
)

# 2. Matcher
matcher_agent = Agent(
    name="Matcher",
    instructions=matcher_instruction,
    model=gemini_model,
)

# 3. Advisor
advisor_agent = Agent(
    name="Advisor",
    instructions=advisor_instruction,
    model=gemini_model,
)

# 4. Notifier
notifier_agent = Agent(
    name="Notifier",
    instructions=notifier_instruction,
    model=gemini_model,
)

watcher_tool = watcher_agent.as_tool(
    tool_name="car_listing_watcher",
    tool_description=(
        "Find and collect new car listings from Craigslist or Facebook Marketplace."
    ),
)
matcher_tool = matcher_agent.as_tool(
    tool_name="car_listing_matcher",
    tool_description="Filter car listings against the user's vehicle preferences.",
)
advisor_tool = advisor_agent.as_tool(
    tool_name="car_mechanical_advisor",
    tool_description=(
        "Score car listings and evaluate reliability, mechanical risks, and specifications."
    ),
)
notifier_tool = notifier_agent.as_tool(
    tool_name="car_listing_notifier",
    tool_description="Create clear alerts and summaries for approved car listings.",
)

# 5. Orchestra Conductor
conductor_agent = Agent(
    name="Orchestra Conductor",
    instructions=conductor_instruction,
    model=gemini_model,
    tools=[watcher_tool, matcher_tool, advisor_tool, notifier_tool],
)

# Aliases
orchestra_conductor = conductor_agent
conductor = conductor_agent
watcher = watcher_agent
matcher = matcher_agent
advisor = advisor_agent
notifier = notifier_agent
agent = conductor_agent

async def main():
    result = await Runner.run(watcher, "scrape a 2017 corolla in san antonio tx for less than 12000")
    return result.final_output
    
        

asyncio.run(main())

