def is_palindrome(check_s):

    return check_s == check_s[::-1]

s = input()
if is_palindrome(s):
    print("Yes")

else:
    print("No")