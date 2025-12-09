class Sensor:
    @staticmethod
    def celsius_to_fahrenheit(temp_c):
        # 靜態方法 (Static Method) - 單位轉換工具
        # 攝氏轉華氏公式: F = C * 9/5 + 32
        return temp_c * 9 / 5 + 32
    
    def __init__(self):
        # 實體屬性 (Instance Attribute) - 記錄該感測器的所有讀數
        self.readings = []
    
    def record(self, temp_c):
        # 實體方法 (Instance Method) - 記錄溫度讀數
        self.readings.append(temp_c)
    
    def avg_fahrenheit(self):
        # 實體方法 (Instance Method) - 計算平均溫度並轉換為華氏
        if not self.readings:
            return 0.0
        
        # 計算平均攝氏溫度
        avg_c = sum(self.readings) / len(self.readings)
        
        # 使用靜態方法轉換為華氏
        avg_f = Sensor.celsius_to_fahrenheit(avg_c)
        
        return avg_f


# 主程式
sensor = Sensor()

n = int(input())
for _ in range(n):
    command = input().strip().split()
    
    if command[0] == "record":
        temp_c = float(command[1])
        sensor.record(temp_c)
    
    elif command[0] == "avg_f":
        result = sensor.avg_fahrenheit()
        print(f"{result:.1f}")
    
    elif command[0] == "convert":
        temp_c = float(command[1])
        result = Sensor.celsius_to_fahrenheit(temp_c)
        print(f"{result:.1f}")
