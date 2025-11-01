shelf_with_books = input().split("&")
while True:
    commands = input()
    if commands == "Done":
        break
    parts = commands.split(" | ")
    command = parts[0]
    if command == "Add Book":
        book_name = parts[1]
        if book_name not in shelf_with_books:
            shelf_with_books.insert(0, book_name)
    elif command == "Take Book":
        book_name = parts[1]
        if book_name in shelf_with_books:
            shelf_with_books.remove(book_name)
    elif command == "Swap Books":
        book1 = parts[1]
        book2 = parts[2]
        if book1 in shelf_with_books and book2 in shelf_with_books:
            index1 = shelf_with_books.index(book1)
            index2 = shelf_with_books.index(book2)
            shelf_with_books[index1], shelf_with_books[index2] = shelf_with_books[index2], shelf_with_books[index1]
    elif command == "Insert Book":
        book_name = parts[1]
        if book_name not in shelf_with_books:
            shelf_with_books.append(book_name)
    elif command == "Check Book":
        index = int(parts[1])
        if index >= 0 and index <= len(shelf_with_books):
            print(shelf_with_books[index])
            
print(", ".join(shelf_with_books))




