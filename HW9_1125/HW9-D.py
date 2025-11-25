N = int(input())

library = [input().strip() for _ in range(N)]
query = input().strip().lower()

found_match = False

for j in range(N):
    original_title = library[j]
    
    lower_title = original_title.lower()
    
    if query in lower_title:
        print(original_title)
        
        found_match = True

if not found_match:
    print("No match found")