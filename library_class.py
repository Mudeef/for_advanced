class Library:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.books = []
    def book_taken(self,book):
        self.books.append(book)
    def book_returned(self,book):
        self.books.remove(book)
    def display(self):
        print(self.name, self.address, self.phone_number)
        print("Books:")
        print(self.books)

obj=Library("Mudeef", "Ayanikkad", "9747200233")
obj.book_taken("Python")
obj.book_taken("Java")
obj.book_taken("C++")
obj.display()
obj.book_returned("Python")
obj.display()
obj.books_returned("C")
obj.display()
obj.book_returned("C")
obj.display()


