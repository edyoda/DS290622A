from book_function import BookFunction

class BookMain:

    def __init__(self,bookfunction_obj):
        self.bookfunction_obj = bookfunction_obj

    def execute(self,choice):
        if choice == 1:
            print("***********Add Book***********")
            self.bookfunction_obj.add_book()

        elif choice == 2:
            print("***********View Book**********")
            self.bookfunction_obj.view_book()

        elif choice == 5:
            print("***********Search Book By ID**********")
            self.bookfunction_obj.search_book_by_id()


if __name__ == "__main__":
    bookfunction_obj = BookFunction()
    bookmain = BookMain(bookfunction_obj)
    
    while True:
        print("Enter \n1.Add Book \n2.View Book \n3.Update Book \n4.Delete Book \n5.Search Book By ID \n6.Search Book by Name \n7.Search Book by Author Name\n")
        choice = int(input("Enter your choice : "))
        bookmain.execute(choice)