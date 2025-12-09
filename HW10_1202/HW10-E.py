import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        """
        計算自身 (self) 與另一點 (other_point) 的距離
        參數 other_point: 預期會傳入另一個 Point 類別的物件
        """
        # 取得兩點座標差
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        
        # 套用距離公式：開根號((x1-x2)^2 + (y1-y2)^2)
        return math.sqrt(dx**2 + dy**2)

# --- 主程式區塊 ---

# 1. 讀取第一行輸入，建立點 A
x1, y1 = map(int, input().split())
point_a = Point(x1, y1)

# 2. 讀取第二行輸入，建立點 B
x2, y2 = map(int, input().split())
point_b = Point(x2, y2)

# 3. 讓 A 去計算與 B 的距離
# 這裡將 point_b 當作參數傳進去，所以在 distance_to 方法內，
# self 代表 point_a，而 other_point 代表 point_b
distance = point_a.distance_to(point_b)

# 4. 輸出結果 (保留 4 位小數)
print(f"{distance:.4f}")