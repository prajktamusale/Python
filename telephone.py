def main():
    """Main function to run the phone directory program."""
    phone_directory = {}
    while True:
        display_menu()
        choice = input("Enter your choice (A-F): ").upper()
        if choice == 'A':
            lookup_number(phone_directory)
        elif choice == 'B':
            add_entry(phone_directory)
        elif choice == 'C':
            edit_number(phone_directory)
        elif choice == 'D':
            delete_entry(phone_directory)
        elif choice == 'E':
            print_directory(phone_directory)
        elif choice == 'F':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def display_menu():
    """Displays the menu of options to the user."""
    print("\nPhone Directory Menu:")
    print("A. Look up a telephone number")
    print("B. Add a new name and telephone number")
    print("C. Edit a telephone number")
    print("D. Delete an entry")
    print("E. Print phone directory in name sequence")
    print("F. Quit")

def lookup_number(phone_directory):
    """Looks up a telephone number by name."""
    name = input("Enter the name to search for: ")
    if name in phone_directory:
        print(f"Telephone number for {name}: {phone_directory[name]}")
    else:
        print(f"Name not found in directory: {name}")

def add_entry(phone_directory):
    """Adds a new name and telephone number to the directory."""
    name = input("Enter the name: ")
    while True:
        try:
            number = int(input("Enter the 2-digit extension (e.g., 12): "))
            if 10 <= number <= 99:
                break
            else:
                print("Invalid extension. Please enter a 2-digit number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    phone_directory[name] = number
    print(f"{name} with extension {number} added to the directory.")

def edit_number(phone_directory):
    """Edits the telephone number associated with an existing name."""
    name = input("Enter the name to edit: ")
    if name in phone_directory:
        while True:
            try:
                new_number = int(input("Enter the new 2-digit extension (e.g., 12): "))
                if 10 <= new_number <= 99:
                    break
                else:
                    print("Invalid extension. Please enter a 2-digit number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        phone_directory[name] = new_number
        print(f"Telephone number for {name} updated to {new_number}.")
    else:
        print(f"Name not found in directory: {name}")

def delete_entry(phone_directory):
    """Deletes an entry (name and number) from the directory."""
    name = input("Enter the name to delete: ")
    if name in phone_directory:
        del phone_directory[name]
        print(f"{name} deleted from the directory.")
    else:
        print(f"Name not found in directory: {name}")

def print_directory(phone_directory):
    """Prints the phone directory in alphabetical order by name."""
    if phone_directory:
        print("\nPhone Directory:")
        for name in sorted(phone_directory.keys()):
            print(f"{name}: {phone_directory[name]}")
    else:
        print("The directory is empty.")

if __name__ == "__main__":
    main()