import os
import shlex


class Terminal:
    def __init__(self):
        self.is_running = True

    def parse_input(self, user_input: str) -> tuple:
        """Strips leading/trailing whitespaces and tokenizes input."""
        tokens = shlex.split(user_input.strip())

        if not tokens:
            return "", []

        command = tokens[0].lower()
        args = tokens[1:]

        return command, args

    def display_help(self) -> None:
        """Prints available built-in commands."""
        print("\n--- T-Shell Commands ---")
        print("  help  - Display available commands")
        print("  clear - Clear the terminal screen")
        print("  exit  - Quit T-Shell\n")

    def execute_command(self, command: str, args: list) -> None:
        """Processes and routes built-in commands."""
        if not command:
            return

        if command == "exit":
            if args:
                print("Error: 'exit' does not take any arguments.")
            else:
                self.is_running = False
                print("Goodbye!")

        elif command == "clear":
            if args:
                print("Error: 'clear' does not take any arguments.")
            else:
                # Clears screen on Windows (cls) or Linux/macOS (clear)
                os.system("cls" if os.name == "nt" else "clear")

        elif command == "help":
            self.display_help()

        else:
            print(f"Error: Unknown command '{command}'. Type 'help' for options.")

    def run(self):
        """Starts the main command loop."""
        print("Welcome to T-Shell! Type 'help' to get started.\n")

        while self.is_running:
            user_input = input("T-Shell> ")
            command, args = self.parse_input(user_input)
            self.execute_command(command, args)