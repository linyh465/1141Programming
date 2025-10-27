str_list = input().strip()

if len(str_list) == 0:
    print("")
else:
    result = ""
    count = 1
    prev_char = str_list[0]
    
    for i in range(1, len(str_list)):
        if str_list[i] == prev_char:
            count += 1
        else:
            result += str(count) + prev_char
            prev_char = str_list[i]
            count = 1
    
    # 處理最後一組字元
    result += str(count) + prev_char
    
    print(result)