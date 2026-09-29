import shlex


class Terminal:
    def __init__(self):
        # The constructor: sets up the state of our object when initialized
        self.is_running = True

    def parse_input(self, user_input: str) -> tuple:
        """Strips leading/trailing whitespaces and tokenizes input."""
        tokens = shlex.split(user_input.strip())

        # If the user just presses Enter without typing anything
        if not tokens:
            return "", []

        # These must be OUTSIDE the 'if not tokens' block
        command = tokens[0].lower()
        args = tokens[1:]

        return command, args

    def run(self):
        """Starts the main command loop."""
        print("Welcome to T-Shell!")

        while self.is_running:
            user_input = input("T-Shell> ")
            command, args = self.parse_input(user_input)

            # Temporary print to test parsing
            if command:
                print(f"Command: '{command}' | Arguments: {args}")