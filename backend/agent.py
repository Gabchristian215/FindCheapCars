import asyncio
import os

from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, Runner, trace
from openai import AsyncOpenAI
from backend.scrape import ScrapeCar
from backend.instructions.matcher import matcher_instruction
from backend.instructions.advisor import advisor_instruction
from backend.instructions.notifier import notifier_instruction

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
    model="gemini-3.8-flash",
    openai_client=gemini_client,
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

# Aliases for direct code orchestration
matcher = matcher_agent
advisor = advisor_agent
notifier = notifier_agent
