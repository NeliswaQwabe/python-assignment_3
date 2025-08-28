# Base class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self._pages = pages  # Encapsulated attribute

    def read(self):
        return f"You start reading '{self.title}' by {self.author}."

    def get_pages(self):  # Encapsulation: using getter method
        return self._pages

    def book_info(self):  # Polymorphic method
        return f"'{self.title}' by {self.author}, {self._pages} pages."

# Derived class (Inheritance)
class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  # in MB

    def download(self):
        return f"Downloading '{self.title}'... ({self.file_size}MB)"

    # Overriding method (Polymorphism)
    def book_info(self):
        return f"E-Book: '{self.title}' by {self.author}, {self._pages} pages, {self.file_size}MB."

# Create objects
physical_book = Book("The Hobbit", "J.R.R. Tolkien", 310)
ebook = EBook("Python 101", "Michael Driscoll", 250, 1.5)

# Use methods
print(physical_book.read())
print(physical_book.book_info())
print("Pages:", physical_book.get_pages())

print(ebook.read())           # Inherited from Book
print(ebook.download())       # Specific to EBook
print(ebook.book_info())      # Overridden method
