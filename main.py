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

    if command == "exit":
        print("Exiting the shell...")
        break 
        print(f"Command received: {command}")
    elif command == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(banner)
    elif command == "help":
        print("Available commands:")
        print("  help  - Show this help message")
        print("  clear - Clear the terminal screen")
        print("  exit  - Exit the shell")
    