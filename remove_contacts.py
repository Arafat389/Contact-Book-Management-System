
def remove_contacts(all_contacts,Name):
        # Remove a book based on its ISBN or title
        for contact in all_contacts:
            if contact['Name'] == Name:
                all_contacts.remove(contact)
                print(f"Book with TITLE  {Name} removed successfully.")
                return
        print(f"No book found with TITLE {Name}.")