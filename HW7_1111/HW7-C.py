'''
def main():
    try:
        domain = input().strip()
    except Exception:
        domain = ""

    try:
        n = int(input().strip())
    except Exception:
        n = 0

    valid = []
    for _ in range(n):
        try:
            email = input().strip()
        except Exception:
            email = ""
        if email.endswith(domain):
            valid.append(email)

    print(valid)

if __name__ == "__main__":
    main()
'''

domain = input().strip()
N = int(input())
email_list = []
for _ in range(N):
    email = input().strip()
    if email.endswith(domain):
        email_list.append(email)
print(email_list)