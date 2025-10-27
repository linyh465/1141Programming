num_list = list(map(int, input().split()))
sum1 = 0
mean1 = 0
median = 0

num_list.sort()
#print(num_list)

for i in range(len(num_list)):
    sum1 += num_list[i]

mean1 = sum1 / len(num_list)

if len(num_list) % 2 == 1:
    median = num_list[len(num_list) // 2]
else:
    median = (num_list[len(num_list) // 2 - 1] + num_list[len(num_list) // 2]) / 2

print("Sum: ", sum1, end=', ')
print(f"Mean: {mean1:.2f}", end=', ')
print(f"Median: {median:.2f}", end='\n')