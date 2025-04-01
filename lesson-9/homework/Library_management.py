class Book:
    def __init__(self,title,author,is_borrowed):
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
                print(f"'{book.title} is already borrowed by someone else")
        else:
            print("You can't borrow books more than three")
    
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
    
    def list_books(self,book):
        if self.books:
            print("Books in the library: ")
            for  book in self.books:
                status="avalaible" if not book.is_borrowed else "borrowed"
                print(f"{book} -- {status}")
        else:
            print("There is no book in the library")
    
    def list_members(self,member):
        if self.members:
            print("Members:")
            for member in self.members:
                print(member)
        else :
            print("No members in the library")
        

        
