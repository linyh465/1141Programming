class Fighter:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self, target):
        """
        攻擊方法：
        self 是攻擊者
        target 是被攻擊者 (另一個 Fighter 物件)
        """
        # 1. 扣除對方的血量
        target.hp -= self.atk
        
        # 2. 輸出攻擊訊息
        print(f"{self.name} attacks {target.name} for {self.atk} damage.")

# --- 主程式區塊 ---

# Helper function: 用來處理輸入並建立戰士物件
def create_fighter():
    line = input().split()
    name = line[0]
    hp = int(line[1])
    atk = int(line[2])
    return Fighter(name, hp, atk)

# 1. 建立兩位戰士
fighter_a = create_fighter()
fighter_b = create_fighter()

# 2. 進入戰鬥迴圈 (While True 代表一直打，直到有人倒下 break)
while True:
    # --- A 攻擊 B ---
    fighter_a.attack(fighter_b)
    
    # 每次攻擊後，立刻檢查 B 是否死亡
    if fighter_b.hp <= 0:
        print(f"{fighter_a.name} wins!")
        break # 戰鬥結束，跳出迴圈

    # --- B 攻擊 A ---
    # 若 B 沒死，換 B 反擊
    fighter_b.attack(fighter_a)
    
    # 檢查 A 是否死亡
    if fighter_a.hp <= 0:
        print(f"{fighter_b.name} wins!")
        break # 戰鬥結束，跳出迴圈