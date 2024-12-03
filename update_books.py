def update_books(all_contacts,title, new_author):
    for book in all_contacts:
        if book['title'] == title:
            old_author = book['author']
            book['author'] = new_author
            print(f"Book author updated from '{old_author}' to '{new_author}'.")
            return
        
    print(f"No book found with TITLE {title}.")
    