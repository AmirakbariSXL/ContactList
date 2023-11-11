class ContactList:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Added {name} to the contact list.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Removed {name} from the contact list.")
        else:
            print(f"{name} not found in the contact list.")

    def display_contacts(self):
        print("\nContact List:")
        for name, number in self.contacts.items():
            print(f"{name}: {number}")

def main():
    my_contacts = ContactList()

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Display Contacts")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            my_contacts.add_contact(name, number)
        elif choice == "2":
            name = input("Enter contact name to remove: ")
            my_contacts.remove_contact(name)
        elif choice == "3":
            my_contacts.display_contacts()
        elif choice == "4":
            print("Exiting the contact list application.")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
