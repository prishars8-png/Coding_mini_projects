def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    print("Please enter the name: ")
    name = input()
    print("Please enter the phone number: ")
    num = input()
    print("Please enter the email: ")
    email = input()
    print("Please enter the address: ")
    address = input()

    if name in contact_book:
        print("Contact already exists!\n")
    else:
        contact_book[name] = {
            "phone": num,
            "email": email,
            "address": address
        }
        print("Contact added successfully!\n")

def view_contact(contact_book):
    print("Please enter the name: ")
    contact_name = input()
    if contact_name in contact_book:
        contact = contact_book[contact_name]
        num = contact.get("phone")
        email = contact.get("email")
        address = contact.get("address")
        '''
        it's look like contact_book = { 
            "Bob" = { ... }
        }
        Nested dictionary, need to get to "Bob" if you want the info. 
        contact = contact_book[contact_name]
        -> go to contact_book and find the contact_name, and save them as 
        contact, and use get() on that. 
        '''

        print(f"Name: {contact_name}")
        print(f"Phone: {num}")
        print(f"Email: {email}")
        print(f"Address: {address}\n")
    else:
        print("Contact not found!\n")

def edit_contact(contact_book):
    print("Please enter the name: ")
    name = input()
    if name in contact_book:
        contact = contact_book[name]
        print("Please enter the new number: ")
        num = input()
        print("Please enter the new email: ")
        email = input()
        print("Please enter the new address: ")
        address = input()

        if num: # python reads "" as false, so this won't run
            contact["phone"] = num
        if email:
            contact["email"] = email
        if address:
            contact["address"] = address
        print("Contact updated successfully!\n")
    else:
        print("Contact not found!\n")

def delete_contact(contact_book):
    print("Please enter the name: ")
    name = input()
    if name in contact_book:
        contact_book.pop(name)
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found!\n")

def list_all_contacts(contact_book):
    if len(contact_book) == 0:
        print("No contacts available.\n")
    else:
        for name in contact_book:
            contact_name = contact_book[name]
            print(f"Name: {name}")
            print(f"Phone: {contact_name.get('phone')}")
            print(f"Email: {contact_name.get('email')}")
            print(f"Address: {contact_name.get('address')}\n")

contact_book = {}
while True:
    display_menu()
    print("\nPlease enter a number from the menu options: ")
    num = int(input())
    if num == 1:
        add_contact(contact_book)
    elif num == 2:
        view_contact(contact_book)
    elif num == 3:
        edit_contact(contact_book)
    elif num == 4:
        delete_contact(contact_book)
    elif num == 5:
        list_all_contacts(contact_book)
    elif num == 6:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")