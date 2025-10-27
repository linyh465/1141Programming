# 讀取密鑰串列和原文
key = list(map(int, input().split()))
plaintext = input()

result = []
key_index = 0  # 追蹤目前使用密鑰串列的哪個位置

for char in plaintext:
    if 'a' <= char <= 'z':
        # 加密小寫字母
        shift = key[key_index % len(key)]
        new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        result.append(new_char)
        key_index += 1
    elif 'A' <= char <= 'Z':
        # 加密大寫字母
        shift = key[key_index % len(key)]
        new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        result.append(new_char)
        key_index += 1
    else:
        # 其他字元（空格、數字等）不加密
        result.append(char)

print(''.join(result))