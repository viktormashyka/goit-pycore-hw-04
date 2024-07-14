def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact with name {name} added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact with name {name} changed."

def show_phone(args, contacts):
    name = args[0]
    return (contacts.get(name))

def show_all(contacts):
    return (contacts)

def help():
    print("\thello - start dialog")
    print("\tadd <name> <phone> - add contact, require name and phone")
    print("\tchange <name> <phone> - change contact, require name and new phone")
    print("\tphone <name> - show phone, require name")
    print("\tall - show all contacts")
    print("\texit or close - exit")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                print(add_contact(args, contacts))
            else: 
                print("Please add name and phone")
        elif command == "change":
            if len(args) == 2:
                name = args[0]
                if name in contacts:
                    print(change_contact(args, contacts))
                else:
                    print(f"Contact with name {name} doesn't exist")
            else: 
                print("Please add name and new phone")
        elif command == "phone":
            if len(args) == 1:
                name = args[0]
                if name in contacts:
                    print(show_phone(args, contacts)) 
                else:
                    print(f"Contact with name {name} doesn't exist")
            else: 
                print("Please add name")           
        elif command == "all":
            if contacts:
                print(show_all(contacts))
            else:
                print("No contacts found")
        elif command == "help":
            help()
        else:
            print("Invalid command.")
        

if __name__ == "__main__":
    main()
    
# Приклад використання:
# Welcome to the assistant bot!
# Enter a command: test
# Invalid command.
# Enter a command: hello
# How can I help you?
# Enter a command: add Mike 0501111111
# Contact added
# Enter a command: change Mike 0502222222
# Contact changed
# Enter a command: phone Mike
# 0502222222
# Enter a command: all
# {"Mike":"0502222222"}
# Enter a command: exit
# Good bye!
