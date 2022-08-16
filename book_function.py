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
            
    def search_book_by_name(self):
        book_name = input("Enter Name of the book you want : ")
        for books in self.booklist:
            if books.book_name == book_name:
                print(books)
                break
        else:
            print("Book not found!")

    def search_book_by_author_name(self):
        book_author_name = input("Enter Author name of the book you want : ")
        for books in self.booklist:
            if books.book_author_name == book_author_name:
                print(books)
                break
        else:
            print("Book not found!")

    def delete_book(self):
        book_id = int(input("Enter Book Id of the book you want to delete : "))
        for books in self.booklist:
            if books.book_id == book_id:
                self.booklist.remove(books)
                print("Successfully Deleted Book")
                break
        else:
            print("No Book Found!")

    def update_book(self):
        book_id = int(input("Enter Book Id of the book you want to update : "))
        for books in self.booklist:
            if books.book_id == book_id:
                book_name = input("Enter Book Name : ")
                book_edition = int(input("Enter Book Edition : "))
                book_author_name = input("Enter Book Author Name : ")
                book_publisher = input("Enter Book Publisher : ")
                book_price = float(input("Enter Book Price : "))
                
                books.set_book_name(book_name)
                books.set_book_edition(book_edition)
                books.set_book_author(book_author_name)
                books.set_book_publisher(book_publisher)
                books.set_book_price(book_price)
                
                print("Successfully Updated Book")
                break
        else:
            print("No Book Found!")




        

