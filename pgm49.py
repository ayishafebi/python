class Publisher:
    def __init__(self):
        self.pid = input("Publisher ID: ")
        self.name = input("Publisher name: ")


class Book(Publisher):
    def __init__(self):
        super().__init__()
        self.title = input("Title: ")
        self.author = input("Author: ")


class Python(Book):
    def display(self):
        self.price = input("Price: ")
        self.pages = input("Pages: ")

        print(self.pid, self.name, self.title,
              self.author, self.price, self.pages)


x = Python()
x.display()
