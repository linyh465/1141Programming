class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

# --- 主程式區塊 ---

# 1. 讀取測試資料筆數
n = int(input())

# 2. 迴圈執行 N 次
for _ in range(n):
    # 讀取單行輸入並分割成寬與高 (使用 map 快速轉換型別)
    w, h = map(int, input().split())
    
    # 建立物件
    rect = Rectangle(w, h)
    
    # 輸出結果
    print(f"Area: {rect.get_area()}, Perimeter: {rect.get_perimeter()}")