import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found!")
        return
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")

def search_contact():
    name = input("Enter name to search: ").lower()
    contacts = load_contacts()
    found_contacts = [c for c in contacts if name in c['name'].lower()]
    
    if found_contacts:
        for contact in found_contacts:
            print(f"{contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")
    else:
        print("No contact found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    contacts = load_contacts()
    
    for contact in contacts:
        if contact['name'].lower() == name:
            contact['phone'] = input("Enter new phone number: ") or contact['phone']
            contact['email'] = input("Enter new email: ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    contacts = load_contacts()
    
    new_contacts = [c for c in contacts if c['name'].lower() != name]
    if len(new_contacts) < len(contacts):
        save_contacts(new_contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
