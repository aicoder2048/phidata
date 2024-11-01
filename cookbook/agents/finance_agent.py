"""Run `pip install yfinance` to install dependencies."""

from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
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

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o", api_key=OPENAI_API_KEY),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Always use tables to display data"],
    markdown=True,
    show_tool_calls=True,
)

# Prompt user for input using Rich
console.print("[bold blue]Welcome to the Finance Agent![/bold blue]")
user_input = Prompt.ask("[yellow]Enter your financial query[/yellow]")

console.print("\n[bold green]Fetching financial data...[/bold green]")
finance_agent.print_response(user_input, stream=True)
