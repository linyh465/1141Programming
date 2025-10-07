usage = int(input())
cost = 0.0
if usage <= 120:
	cost = usage * 2.10
elif usage <= 300:
	cost = 120 * 2.10 + (usage - 120) * 3.02
else:
	cost = 120 * 2.10 + 180 * 3.02 + (usage - 300) * 4.39
    
print(f"{cost:.2f}")
