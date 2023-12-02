class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone Number: {contact.phone_number}")
            print(f"Email: {contact.email}")
            print("--------------------")

# Example usage
contact_book = ContactBook()

contact1 = Contact("John Doe", "1234567890", "john.doe@example.com")
contact2 = Contact("Jane Smith", "9876543210", "jane.smith@example.com")

contact_book.add_contact(contact1)
contact_book.add_contact(contact2)

contact_book.display_contacts()
