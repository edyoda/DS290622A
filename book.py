class Book:

    def __init__(self,book_id,book_name,book_edition,book_author_name,book_publisher,book_price):
        self.book_id = book_id
        self.book_name = book_name
        self.book_edition = book_edition
        self.book_author_name = book_author_name
        self.book_publisher = book_publisher
        self.book_price = book_price

    def __str__(self):
        return f"Book ID : {self.book_id} \nBook Name : {self.book_name} \nBook Edition : {self.book_edition} \nBook Author Name : {self.book_author_name} \nBook Publisher : {self.book_publisher} \nBook Price : {self.book_price}"


    def set_book_id(self,book_id):
        self.book_id = book_id

    def get_book_id(self):
        return self.book_id

    def set_book_name(self,book_name):
        self.book_name = book_name

    def get_book_name(self):
        return self.book_name

    def set_book_edition(self,book_edition):
        self.book_edition = book_edition

    def get_book_edition(self):
        return self.book_edition

    def set_book_author(self,book_author_name):
        self.book_author_name = book_author_name

    def get_book_author(self):
        return self.book_author_name
            
    def set_book_publisher(self,book_publisher):
        self.book_publisher = book_publisher

    def get_book_publisher(self):
        return self.book_publisher

    def set_book_price(self,book_price):
        self.book_price = book_price

    def get_book_price(self):
        return self.book_price
    