print("Welcome to PTCL")

def PTCL(input):
    
        match(input):
            case 1:
                print("hello\n")
            case 2:
                print("by")

            
user_input=""
while user_input!="exit":
    try:
        user_input=input("Press 1 to start a new complain\nPress 2 for Live chat\n")
        PTCL(user_input)
    except ValueError:
        print("Don't ruin my program\n")