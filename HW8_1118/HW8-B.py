# Read N (number of fruit entries)
n = int(input())

# Build the price dictionary
price_dict = {}
for _ in range(n):
    line = input().split()
    fruit_name = line[0]
    price = int(line[1])
    price_dict[fruit_name] = price

# Read M (number of queries)
m = int(input())

# Process queries and output prices
for _ in range(m):
    fruit_name = input()
    print(price_dict[fruit_name])
