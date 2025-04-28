# **************************ДЕКОРАТОР*********************************
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me the name and the phone please."
        except IndexError:
            return "Give me the name of the contact please."
        except KeyError:
            return "Give me the right name of the contact please."
    return inner

# **************************ФУНКЦІОНАЛ********************************
@input_error
def parse_input(user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if not name in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return "This contact is already exists"

@input_error
def show_all(contacts):
    if contacts == {}:
        return "There isn't any contact"
    else:
        return "All contacts:", contacts

@input_error    
def show_phone(args, contacts):
    name = args[0]
    return f"{name} phone number is: {contacts[name]}" 
    
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "This contact isn't exists. Try to add it!"
    
# *************************ГОЛОВНА ФУНКЦІЯ***********************************
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
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
