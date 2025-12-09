class Book:
    # 類別屬性 (Class Attribute) - 總藏書量
    total_books = 0
    
    def __init__(self, name, isbn):
        # 實體屬性 (Instance Attribute)
        self.name = name
        self.isbn = isbn
        
        # 建立書籍時，總藏書量 +1
        Book.total_books += 1
    
    @staticmethod
    def is_valid_isbn(isbn):
        # 靜態方法 (Static Method) - 驗證 ISBN
        # 檢查是否全為數字且長度為 10 或 13
        if not isbn.isdigit():
            return False
        return len(isbn) == 10 or len(isbn) == 13


# 主程式
n = int(input())
for _ in range(n):
    command = input().strip().split()
    
    if command[0] == "add":
        book_name = command[1]
        isbn = command[2]
        
        # 先用靜態方法驗證 ISBN
        if Book.is_valid_isbn(isbn):
            # 驗證通過，建立書籍物件
            book = Book(book_name, isbn)
            print(f"Added {book_name}, Total Books: {Book.total_books}")
        else:
            # 驗證失敗
            print("Invalid ISBN")
