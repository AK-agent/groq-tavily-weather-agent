from google.adk.agents import Agent
from google.adk.tools.langchain_tool import LangchainTool
from google.adk.models.lite_llm import LiteLlm
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
import requests

from dotenv import load_dotenv
load_dotenv()  # still useful if you keep TAVILY_API_KEY in .env

# ── Simple free weather tool (wttr.in) - no API key needed ──
@tool
def get_weather(location: str) -> str:
    """Get current weather for a city (free, no API key)"""
    try:
        url = f"https://wttr.in/{location.replace(' ', '+')}?format=3"
        return requests.get(url, timeout=5).text.strip()
    except:
        return "Sorry, couldn't get the weather right now"


# ── LLM Setup ───────────────────────────────────────────────────
llm = LiteLlm(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=4096,
)

# ── Tools ───────────────────────────────────────────────────────
tavily_search = TavilySearchResults(max_results=5)

# Wrap tools for ADK
tavily_tool = LangchainTool(tool=tavily_search)
weather_tool = LangchainTool(tool=get_weather)

# ── Create Agent ────────────────────────────────────────────────
root_agent = Agent(
    name="groq_tavily_free_weather_agent",
    model=llm,
    description="Agent that can search the web (Tavily) and get current weather — completely free",
    instruction="""You are a helpful assistant with two main capabilities:

1. General web/information search → use the tavily_tool tool
2. Current weather information → use the weather_tool tool

When user asks about weather, temperature, rain, wind, how's the weather etc.
→ use weather_tool tool with the city/location name

For everything else → use tavily_tool search tool.""",
    tools=[tavily_tool, weather_tool]
)