s = input()
v = "aeiouAEIOU"
result = ""

for c in s:
    if c == " ":
        result += " "
    elif c in v:
        result += c.upper()
    else:
        result += c.lower()
print(result)