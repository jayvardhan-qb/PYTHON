'''
Create a contact book using dictionaries to store and manage names,
phone numbers, and emails.
'''

def menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Show all contacts")
    print("6. Exit")

contact_book = {}

def add_contact():
    name = input("Enter Name: ").strip()
    if name in contact_book:
        print("This name already exists. Try something different.")
    else:
        phone = int(input("Enter phone number (0-9): "))
        email = input("Enter email: ").strip()
        contact_book[name] = {'phone': phone, 'email': email}

        print("Contact added successfully!")

def update_contact():
    name = input("Enter name: ").strip()
    if name in contact_book:
        phone = int(input("Enter new phone number: "))
        email = input("Enter new email: ").strip()
        contact_book[name] = {'phone': phone, 'email': email}
        print(f"Contact {name} updated successfully!")
    else:
        print(f"No contact with {name} found.")

def remove_contact():
    name = input("Enter name: ").strip()
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print(f"No contact with name {name} found.")

def search_contact():
    name = input("Enter name: ").strip()
    contact = contact_book.get(name)
    if contact:
        print(f"Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print(f"No contact with name {name} found.")

def show_all_contacts():
    if not contact_book:
        print("No contacts found.")
    else:
        print("\nContacts:")
        for name, info in contact_book.items():
            print(f"{name}, {info['phone']}, {info['email']}")

def main():

    while True:
        menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            update_contact()
        elif choice == '3':
            remove_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            show_all_contacts()
        elif choice == '6':
            print("Exiting!!")
            break
        else:
            print("Invalid choice selection. Try Again.")

if __name__ == '__main__':
    main()