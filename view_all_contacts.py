def view_all_contacts(all_contacts):
    if all_contacts != []:
        for contact in all_contacts:
            print(f"Name: {contact['Name']} | Email: {contact['Email']} | Phone_Number: {contact['Phone_Number']} | Address: {contact['Address']} ")


    else:
        print("No Books found in program")