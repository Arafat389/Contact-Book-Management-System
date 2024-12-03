
def save_all_contacts(all_contacts):
    with open ("all_contacts.csv","w") as fp:
        for contact in all_contacts:
            line = f"{contact['Name']} , {contact['Email']} , {contact['Phone_Number']} , {contact['Address']}  , \n"
            fp.write(line)