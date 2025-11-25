def analyze_expenses():
    # 1. 讀取 N (商品數量)
    try:
        N = int(input())
    except Exception:
        N = 0
        
    # 2. 使用字典來儲存每個類別的總花費
    # 格式: { 'Category': total_price, ... }
    category_totals = {}

    # 3. 讀取 N 筆商品資料並計算總和
    for _ in range(N):
        try:
            # 讀取 Category Item Price，並以空白分隔
            line = input().split()
            if len(line) < 3:
                continue # 忽略格式不完整的行
                
            category = line[0]
            # Item 是 line[1]，但在計算中不需要用到
            price = int(line[2])
            
            # 聚合計算：如果類別已存在，則加上價格；否則，初始化為價格
            if category in category_totals:
                category_totals[category] += price
            else:
                category_totals[category] = price
                
        except EOFError:
            break
        except ValueError:
            # 忽略價格非數字的資料行
            continue
    
    # 如果沒有任何有效的資料 (N=0 或所有資料格式錯誤)
    if not category_totals:
        print("Highest: (0)")
        return

    # 4. 找出花費最高的類別 (Highest)
    
    # 4a. 找到最高的金額 (max_amount)
    # values() 取得所有金額，max() 找出最大值
    max_amount = max(category_totals.values())
    
    # 4b. 找出所有達到最高金額的類別 (可能有多個)
    highest_categories = []
    for category, total in category_totals.items():
        if total == max_amount:
            highest_categories.append(category)
            
    # 4c. 根據題目要求：如果有多個類別並列最高，任選一個即可。
    # 為了程式碼的確定性，我們選定字母順序第一個的類別來輸出。
    highest_categories.sort()
    highest_category_name = highest_categories[0]

    # 5. 輸出第一行：花費最高的類別及其金額
    print(f"Highest: {highest_category_name} ({max_amount})")

    # 6. 輸出剩餘的類別總花費 (依類別名稱字母順序排序)
    
    # 6a. 取得所有類別名稱，並按字母順序排序
    sorted_categories = sorted(category_totals.keys())
    
    # 6b. 依序輸出結果
    for category in sorted_categories:
        total = category_totals[category]
        print(f"{category}: {total}")

# 執行函式
analyze_expenses()