sequence_of_targets = [int(target) for target in input().split()]
command = input().split()
while command[0] != "End":
    action, index, value = command[0], int(command[1]), int(command[2])
    if action == "Shoot":
        if index in range(len(sequence_of_targets)):
            sequence_of_targets[index] -= value
            if sequence_of_targets[index] <= 0:
                del sequence_of_targets[index]
    elif action == "Add":
        if index in range(len(sequence_of_targets)):
            sequence_of_targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if index - value not in range(len(sequence_of_targets)) or index + value not in range(len(sequence_of_targets)):
            print("Strike missed!")
        else:
            before_strike = sequence_of_targets[:index - value]
            after_strike = sequence_of_targets[index + value + 1:]
            sequence_of_targets = before_strike + after_strike
    command = input().split()
print(*sequence_of_targets, sep = "|")