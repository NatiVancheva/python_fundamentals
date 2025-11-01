tourists = int(input())
wagons = list(map(int, input().split()))
max_capacity = 4

for i in range(len(wagons)):
    free = max_capacity - wagons[i]
    if free > 0 and tourists > 0:
        to_board = min(free, tourists)
        wagons[i] += to_board
        tourists -= to_board

if tourists == 0 and any(w < max_capacity for w in wagons):
    print("The lift has empty spots!")
elif tourists > 0:
    print(f"There isn\'t enough space! {tourists} people in a queue! ")

print(" ".join(map(str, wagons)))