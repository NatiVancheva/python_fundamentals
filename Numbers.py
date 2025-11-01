numbers = list(map(int, input().split()))
average_number = sum(numbers) / len(numbers)
new_numbers = [number for number in numbers if number > average_number]
if new_numbers:
    top_five_nums = sorted(new_numbers,reverse=True)[:5]
    print(' '.join(map(str, top_five_nums)))
else:
    print("No")

