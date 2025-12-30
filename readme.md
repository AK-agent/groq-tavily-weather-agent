# Groq + Tavily + Free Weather Agent

A simple, **completely free** AI agent built with:

- **Groq** (fast LLM inference)
- **Llama-3.3-70B-Versatile** (or other strong tool-calling model)
- **Tavily** (web search)
- **wttr.in** (free weather API, no key needed)

Powered by Google's ADK (Agent Development Kit) + LiteLLM.

## Features

- Ask general questions → gets answers via Tavily web search
- Ask about current weather / temperature / rain / wind → uses free wttr.in service
- No paid weather APIs required
- Very fast inference thanks to Groq

## Current Setup (Dec 2025 recommendation)

```text
Model:           groq/llama-3.3-70b-versatile  (strongly recommended over 8b)
Tavily:          Free tier (limited requests)
Weather:         wttr.in (no API key, very reliable)
Important: The 8B models (including llama-3.1-8b-instant) have very poor tool calling reliability.
Always prefer 70B-class versatile/instruct models for agents.
Installation

Clone the repository

Bashgit clone https://github.com/YOUR_USERNAME/groq-tavily-weather-agent.git
cd groq-tavily-weather-agent

Install dependencies

Bashpip install -r requirements.txt
# or if you prefer poetry / pdm / uv etc.

Create .env file

Bashcp .env.example .env
Then edit .env and add your Tavily API key:
envTAVILY_API_KEY=tvly-yourkeyhere123...
Usage
Bashpython main.py
# or however you run your agent script
Example questions that work well:

What's the weather like in Kyoto right now?
Is it raining in Paris?
Current temperature in Mysore?
Tell me the latest news about SpaceX
Who won the last Nobel Prize in Physics?

Project Structure
text.
├── main.py                 # Entry point / agent initialization
├── .env                    # Your secrets (gitignore'd)
├── .env.example
├── requirements.txt
└── README.md
Requirements
textgoogle-adk>=0.1.0
litellm>=1.0.0
langchain-community
langchain
requests
python-dotenv
tavily-python
Troubleshooting
Tool calling fails / weird XML tags?
→ Switch to llama-3.3-70b-versatile or llama-4-maverick-...
The 8B models are not reliable for tool use in late 2025.
License
MIT