


from save_all_contacts import save_all_contacts

def add_contact(all_contacts):
    Name = input("Enter user Name: ")
    Email = input("Enter Email: ")
    Phone_Number = int(input("Enter Phone_Number: ")) 
    Address = str(input("Enter your Address: ")) 
    
    contact = {
        "Name":Name,
        "Email":Email,
        "Phone_Number":Phone_Number,
        "Address":Address,

    }

    all_contacts.append(contact)
    save_all_contacts(all_contacts)
    print("Books added successfully")
    return all_contacts