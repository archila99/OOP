 # aggregation = represents a relationship where one object(the whole) containse refernces to one or more INDEPENDENT objects (the parts)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def print_book(self):
        for book in self.books:
            print(book)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"

library = Library("Cardiff Publick Library")

book1 = Book("Harry Potter, Stone", "J.K Rowling")
book2 = Book("The Hobbit", "J.R.R Tolkein")
book3 = Book("Doctor House", "Hawkings")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.print_book()


