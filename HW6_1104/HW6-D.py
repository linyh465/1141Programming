def is_palindrome(normalized_s):
    
    # Check if the normalized string is equal to its reverse
    return normalized_s == normalized_s[::-1]

s = input()
if is_palindrome(s):
    print("Yes")

else:
    print("No")