"""Run `pip install openai duckduckgo-search python-dotenv rich` to install dependencies."""

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from rich.console import Console
from rich.prompt import Prompt
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Get OPENAI_API_KEY from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Initialize Rich console
console = Console()

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o-mini", api_key=OPENAI_API_KEY),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    debug_mode=True,
)

# Prompt user for input using Rich
console.print("[bold blue]Welcome to the Web Agent![/bold blue]")
user_input = Prompt.ask("[yellow]Enter your search query[/yellow]")

console.print("\n[bold green]Searching the web...[/bold green]")
web_agent.print_response(user_input, stream=True)

