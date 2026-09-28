#import shlex
#import os
class Terminal:
    def __init__ (self):#The constructor it sets up the state of our object when initialized
        self.is_running= True
    def run(self):#the main method that keep the terminal alive
        "Starts the main command loop."
        print("Welcome to T-shell!")    

        while self.is_running:#an instance variable tracking shell state when set to false the loops stops
            user_input=input("T-shell>")
            print(f"You typed:{user_input}")
            

"""while True:
    command = input("@tshell:~$ ").strip()

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
    elif cmd == "pwd":
        print(os.getcwd())
    elif cmd == "ls":
        try:
            target_dir = args[0] if args else "."
            files = os.listdir(target_dir)
            for file in files:
                print(file)
        except Exception as e:
            print(f"Error: {e}")
    elif cmd == "help":
        print("Available commands:")
        print("  clear - Clear the terminal screen")
        print("  pwd   - Print the current working directory")
        print("  ls    - List files and directories in the current directory")
        print("  help  - Show this help message")
        print("  exit  - Exit the shell")
    else:
        print(f"Unknown command received: {cmd} (Arguments:{args})")"""

    