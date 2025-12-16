class Library:
    def __init__(self):
        self.borrowed_books = set()
        self.members = {}
    
    @staticmethod
    def check_available(isbn, borrowed_books):
        """檢查書籍是否可借"""
        return isbn not in borrowed_books
    
    @staticmethod
    def borrow_book(isbn, date, member, borrowed_books):
        """借書：添加到borrowed_books和member history"""
        borrowed_books.add(isbn)
        member.add_history(isbn, date)
    
    @staticmethod
    def return_book(isbn, borrowed_books):
        """還書：從borrowed_books中移除"""
        borrowed_books.discard(isbn)

class Member:
    def __init__(self, name):
        self.name = name
        self.history = []
    
    def add_history(self, isbn, date):
        """添加借書記錄"""
        self.history.append((isbn, date))
    
    def show_history(self):
        """顯示借書歷史"""
        for isbn, date in self.history:
            print(f"{date}: {isbn}")

library = Library()

n = int(input())
for _ in range(n):
    command = input().split()
    
    if command[0] == "borrow":
        user = command[1]
        isbn = command[2]
        date = command[3]
        
        # Create member if not exists
        if user not in library.members:
            library.members[user] = Member(user)
        
        # Check if available and borrow
        if Library.check_available(isbn, library.borrowed_books):
            Library.borrow_book(isbn, date, library.members[user], library.borrowed_books)
            print("Borrowed")
        else:
            print("Unavailable")
    
    elif command[0] == "return":
        isbn = command[1]
        Library.return_book(isbn, library.borrowed_books)
    
    elif command[0] == "history":
        user = command[1]
        if user in library.members:
            library.members[user].show_history()
