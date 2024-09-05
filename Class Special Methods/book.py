# Classes in Python can implement certain operations with special method names.
# These methods are not actually called directly,
# but by Python specific language syntax.

class Book():
    def __init__(self, title, author, pages):
        print ("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s , Author: %s, Pages: %s " %(self.title, self.author, self.pages)
        # We could also use a format() function...

    def __len__(self):
        return self.pages

    def __del__(self):
        print ("A book is destroyed")

book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)
print(len(book))
del book
