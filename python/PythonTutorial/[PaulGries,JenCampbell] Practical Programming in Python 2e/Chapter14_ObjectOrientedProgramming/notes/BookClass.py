

# note: methods belong to classes, so Book.numAuthors(book1) passes
# note: instance variables belong to objects, so Book.title fails.

class Book:
    """Information about a book, including title, list of authors,
        publisher, ISBN, and price. """

    def __init__(self, title, authors, publisher, isbn, price):
        self.title = title
        self.authors = authors[:] # copy, not direct reference
        self.publisher = publisher
        self.ISBN = isbn
        self.price = price

    def __str__(self):
        authorsStr = "\n -" + "\n -".join(self.authors)
        return "Title: {0}\nAuthors: {1}\nPublisher: {2}\nISBN: {3}\nPrice: {4}"\
            .format(self.title, authorsStr, self.publisher, self.ISBN, self.price)

    def __eq__(self, other):
        return self.ISBN == other.ISBN


    def numAuthors(self):
        """Return number of authors of this book."""
        return len(self.authors)


if __name__ == "__main__":
    pythonBook = Book(title="Practical Programming", authors=["Campbell", "Gries", "Montojo"],
                      publisher="Pragmatic Bookshelf", isbn="978-1-93778-545-1", price=25.0)
    adventureBook = Book(title="Ranger's Apprentice", authors=["John Flanagan"], publisher="Penguin",
                         isbn="111-1-11111-111-1", price=24.0)
    print(pythonBook)
    print(pythonBook.numAuthors())
    print(pythonBook == adventureBook)
    print(pythonBook.__dict__)
