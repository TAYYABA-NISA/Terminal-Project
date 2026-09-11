import shlex
import os

banner = """
╔══════════════════════════════════╗
║          T-SHELL v1.0            ║
║      Your Custom Terminal        ║
╚══════════════════════════════╝
"""
print(banner)

while True:
    command = input("TAZWAZ@tshell:~$ ").strip()

    if not command:
        continue
    try:
        command = shlex.split(command)#split() break the compond words into the single words
    except ValueError:
        print("Error: Invalid command syntax.")
        continue
    cmd = command[0].lower()
    args=command[1:]

    if cmd == "exit":
        print("Exiting the shell...")
        break 
    elif cmd == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
    elif cmd == "help":
        print("Available commands:")
        print("  help  - Show this help message")
        print("  clear - Clear the terminal screen")
        print("  exit  - Exit the shell")
    else:
        print(f"Unknown command received: {cmd} (Arguments:{args})")

    