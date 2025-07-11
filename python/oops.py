class Book:

    

    def __init__(self, title, author , price):
        self.title = title
        self.author = author
        self.price = price

    def get_book_details(self):
        print(f"the details of book are: {self.title},' ' ,{self.author},'',{self.price}")

book1 = Book("The Alchemist", "Paulo Coelho", 300)
book1.get_book_details