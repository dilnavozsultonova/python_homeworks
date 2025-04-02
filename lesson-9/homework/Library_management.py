class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed=False

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Member:
    def __init__(self,name):
        self.name=name
        self.borrowed_books=[]

    def borrow_book(self,book):
        if len(self.borrowed_books)<3:
            if not book.is_borrowed:
                self.borrowed_books.append(book)
                print(f"{self.name}  borrowed successfully '{book.title}'")
                book.is_borrowed=True
            else:
                BookAlreadyBorrowedException
        else:
            MemberLimitExceededException
    
    def return_book(self,book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed=False
            print(f"{self.name} has returned '{book.title}'")
        else:
            print(f"'{book.title}' is not borrowed")

    def __str__(self):
        return f"Member : {self.name}"


class Library:
    def __init__(self):
        self.books=[]
        self.members=[]
    
    def add_books(self,book):
        self.books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def add_member(self,member):
        self.members.append(member)
        print("{self.member} is added to the list of members successfully")
    
    def list_books(self):
        if self.books:
            print("Books in the library: ")
            for  book in self.books:
                status="avalaible" if not book.is_borrowed else "borrowed"
                print(f"{book} -- {status}")
        else:
            raise BookNotFoundError
    
    def list_members(self):
        if self.members:
            print("Members:")
            for member in self.members:
                print(member)
        else :
            print("No members in the library")
        


      
class BookNotFoundError(Exception):
    pass

try:
    print("Book not found")
    raise BookNotFoundError("The requested book was not found in the library.")  # Optional message
except BookNotFoundError as e:
    print(f"Error raised: {e}")

class BookAlreadyBorrowedException(Exception):
    pass
try:
    print("Book is already borrowed")
    raise BookAlreadyBorrowedException("Book is already borrowed by someone else")
except BookAlreadyBorrowedException as e:
    print(f"Error raised: {e} ")


class MemberLimitExceededException(Exception):
    pass
try:
    print("You can only borrow limited number of books")
    raise MemberLimitExceededException("You can't take more than three books!!!")
except MemberLimitExceededException as e:
    print(f"Error raised {e}")

library = Library()

# Adding books to the library
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book4 = Book("Moby-Dick", "Herman Melville")

library.add_books(book1)
library.add_books(book2)
library.add_books(book3)
library.add_books(book4)

member1 = Member("Alice")
member2 = Member("Bob")

library.add_member(member1)
library.add_member(member2)

# Listing books and members
library.list_books()
library.list_members()

# Borrowing and returning books
member1.borrow_book(book1)
member1.borrow_book(book2)
member1.borrow_book(book3)
member1.borrow_book(book4)  # This should print a message about borrowing limit

member1.return_book(book2)
member1.borrow_book(book4)  # Now Alice can borrow Moby-Dick

# Listing the books again to see the updates
library.list_books()