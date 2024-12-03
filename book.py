import add_contacts
import view_all_contacts
import update_books
import remove_contacts
all_contacts = []

while True:    # using multiple running
    print("Contact Book Management System")
    print("0. Exit")
    print("1. Add Contacts")
    print("2. View Contacts")
    print("3. Prevent Duplicate Numbers")
    print("4. Remove Contacts")
    

    menu  = input("Select any number: ")

    if menu == "0":
        print("Thanks for using  Contact Book Management system") 
        break

    elif menu == "1":
         all_books = add_contacts.add_contact(all_contacts)
    elif menu == "2":
         view_all_contacts.view_all_contacts(all_contacts)

    elif menu == "3":
         title = input("Enter title to Update: ")
         new_author = input("Enter New author Name: ")
         update_books.update_books(all_contacts,title, new_author)


    elif menu == "4":
         Name = input("Enter Name Remove: ")
         
         remove_contacts.remove_contacts(all_contacts,Name)         

    else:
         print("Choose a valid number")          
