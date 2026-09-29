class Terminal:
    def __init__ (self):#The constructor it sets up the state of our object when initialized
        self.is_running= True
    def run(self):#the main method that keep the terminal alive
        "Starts the main command loop."
        print("Welcome to T-shell!")    

        while self.is_running:#an instance variable tracking shell state when set to false the loops stops
            user_input=input("T-shell>")
            print(f"You typed:{user_input}")