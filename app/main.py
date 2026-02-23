from rich.console import Console
from rich.prompt import Prompt
from app.llm.gemini_client import GeminiClient
from app.memory.session import SessionMemory

console = Console()


def run_chat():
    console.print("[bold green]PartnerAI Initialized.[/bold green]")
    console.print("Type 'exit' to quit.\n")

    client = GeminiClient()
    memory = SessionMemory()

    while True:
        user_input = Prompt.ask("[bold blue]You[/bold blue]")

        if user_input.lower() in ["exit", "quit"]:
            console.print("[bold red]Exiting PartnerAI.[/bold red]")
            break

        memory.add_user_message(user_input)

        response = client.send_message(user_input)

        memory.add_ai_message(response)

        console.print(f"[bold magenta]PartnerAI:[/bold magenta] {response}\n")


if __name__ == "__main__":
    run_chat()