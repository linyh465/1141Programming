class GameServer:
    # 類別屬性 (Class Attribute) - 全服經驗值倍率
    exp_rate = 1.0
    
    @classmethod
    def set_event_rate(cls, rate):
        # 類別方法 (Class Method) - 設定全服倍率
        cls.exp_rate = rate
    
    @staticmethod
    def is_valid_name(name):
        # 靜態方法 (Static Method) - 過濾髒話
        # 名字不能包含 "bad"
        return "bad" not in name.lower()
    
    def __init__(self, name):
        # 實體屬性 (Instance Attribute) - 玩家資訊
        self.name = name
    
    def gain_exp(self, monster_xp):
        # 實體方法 (Instance Method) - 計算經驗值
        # 經驗值 = 怪物基礎經驗 * 全服倍率
        actual_xp = int(monster_xp * GameServer.exp_rate)
        return actual_xp


# 主程式
n = int(input())
for _ in range(n):
    command = input().strip().split()
    
    if command[0] == "player":
        player_name = command[1]
        monster_xp = int(command[2])
        
        # 先檢查名字是否合法
        if not GameServer.is_valid_name(player_name):
            print("Banned Name")
        else:
            # 建立玩家並計算經驗值
            player = GameServer(player_name)
            actual_xp = player.gain_exp(monster_xp)
            print(f"{player_name} gained {actual_xp} XP")
    
    elif command[0] == "event":
        new_rate = float(command[1])
        GameServer.set_event_rate(new_rate)
        print("Global Rate Updated")
