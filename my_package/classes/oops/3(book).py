class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def display_details(self):
        print("\nBook Details")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"ISBN: {self.isbn}")

title = input("Enter book title: ")
author = input("Enter author name: ")
year = input("Enter publication year: ")
isbn = input("Enter ISBN number: ")

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def display_details(self):
        print("\nBook Details")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"ISBN: {self.isbn}")

title = input("Enter book title: ")
author = input("Enter author name: ")
year = input("Enter publication year: ")
isbn = input("Enter ISBN number: ")

book1 = Book(title, author, year, isbn)
book1.display_details()

