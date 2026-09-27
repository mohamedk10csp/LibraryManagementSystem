from book import Book


def add_book(library):
    """Add a new book to the library."""
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    isbn = input("Enter the book ISBN: ")

    new_book = Book(title, author, isbn)
    library.append(new_book)

    print("Book added successfully")


def list_books(library):
    """Show all books in the library."""
    if len(library) == 0:
        print("No books in the library.")
    else:
        for book in library:
            print (book)


def find_book(library, query):
    """Find a book by title or the author in the library."""
    for book in library:
        if book.title == query or book.author == query:
            return book
    return None

if __name__ == "__main__":
    my_library = []

    while True:
        print("\nLibrary Manager")
        print("1. Add a New Book")
        print("2. List all Books")
        print("3. Find Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(my_library)
        elif choice == "2":
            list_books(my_library)
        elif choice == "3":
            search = input("Enter the book title or author: ")
            found_book = find_book(my_library, search)
            if found_book:
                print("Book found:")
                print(found_book)
            else:
                print("Book not found.")
        elif choice == "4":
            print("Byebye!")
            break
        else:
            print("Invalid choice.")