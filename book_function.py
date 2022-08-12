from book import Book

class BookFunction:
    booklist = []
    def add_book(self):
        book_id = int(input("Enter Book Id : "))
        book_name = input("Enter Book Name : ")
        book_edition = int(input("Enter Book Edition : "))
        book_author_name = input("Enter Book Author Name : ")
        book_publisher = input("Enter Book Publisher : ")
        book_price = float(input("Enter Book Price : "))
        book_obj = Book(book_id,book_name,book_edition,book_author_name,book_publisher,book_price)
        self.booklist.append(book_obj)
        print("Book Successfully Added!")

    def view_book(self):
        for i in self.booklist:
            print()
            print(i)

    def search_book_by_id(self):
        book_id = int(input("Enter Book Id of the book you want : "))
        for books in self.booklist:
            if books.book_id == book_id:
                print(books)
                break
        else:
            print("Book not found!")
            


