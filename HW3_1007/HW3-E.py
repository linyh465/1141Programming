Y = int(input())
# 閏年判斷

leap = (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0)

if leap:
	d_sum = sum(int(d) for d in str(Y))
	if d_sum % 3 == 0:
		print("超級閏年")
	else:
		print("普通閏年")
else:
	print("平年")
