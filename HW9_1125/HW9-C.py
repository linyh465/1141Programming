import math
def calculate_share(amount, people):
    total = math.floor(amount * 1.1)
    per = math.ceil(total / people)
    return total, per

amount, people = map(int,input().split())
total, per = calculate_share(amount, people)
print(f"Total: {total}, Per person: {per}")