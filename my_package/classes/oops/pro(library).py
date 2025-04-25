class Library:
    def __init__(self):
        self.books = ["Python Basics","Data Structures", "AI for Beginners", "Machine Learning",]

    def view_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(f" {book}")

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"\nYou have borrowed '{book_name}'. Please return it after reading.")
        else:
            print(f"\nThis! '{book_name}' is not available in the library.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"\nThanks for returning '{book_name}'. It is now available in the library again.")

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"\nThe book '{book_name}' has been added to the library.")

lib = Library()

# Menu
while True:
    print("\n===== Library Menu =====")
    print("1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Add Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        lib.view_books()
    elif choice == "2":
        name = input("Enter the book name to borrow: ")
        lib.borrow_book(name)
    elif choice == "3":
        name = input("Enter the book name to return: ")
        lib.return_book(name)
    elif choice == "4":
        name = input("Enter the new book name to add: ")
        lib.add_book(name)
    elif choice == "5":
        print("Thank you for using the Library System!")
        break
    else:
        print("Invalid choice. Please try again.")
