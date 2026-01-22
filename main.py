import os

# In this project i will attempt to make a "logger"/journal that takes input from a user and allows them to save their entries in the logger.
# This is done in order for me to learn how python handles files, texts & storing information.
print("Hi")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def new_text():
    file_name = ""
    user_input = input("> ").tostring()
    with open(file_name, "a") as n:
        n.write("\n")
        n.write(user_input)

def remove_entry():
    file_name = ""

def new_entry():
    file_name =""
        
def main():
    while True:
        # Display menu
        print("____________________________")
        print("| What would you like to do? |")
        print("____________________________")
        print("> Make a new entry [1]")
        print("> Remove an entry [2]")
        print("> Edit an entry [3]")
        print("> Exit [4]")
        userChoice = input("").toString()
        match userChoice:
            case 1:
                print("1")
                new_entry()
            case 2:
                print("2")
                remove_entry()
            case 3:
                print("3")

            case 4:
                print("4")
                exit()    
            case _:
                print("That is not a valid option. \n Press [Enter] to continue.")
                return







if __name__ =="__main__":
    main()

