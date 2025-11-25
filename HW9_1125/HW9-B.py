goal = int(input())

all_steps = []

steps_list = input().split()


for step in steps_list:
    all_steps.append(int(step))

steps_sum = sum(all_steps)


print(f"Total: {steps_sum}")


if steps_sum >= goal:
    print("Goal Achieved!")
else:
    print("Keep Walking!")