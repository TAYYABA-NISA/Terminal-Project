print("Welcome to TAZWAZ Shell!")
while True:
    command = input("TAZWAZ@tshell:~$ ")

    if command == "exit":
        print("Exiting the shell...")
        break 

    print(f"Command received: {command}")