def filter_by_threshold(numbers, limit):
    return [num for num in numbers if num > limit]


input_numbers = list(map(int, input().split()))
threshold = int(input())

filtered_numbers = filter_by_threshold(input_numbers, threshold)

print(filtered_numbers)