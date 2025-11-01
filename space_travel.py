travel_route = input().split("||")
starting_amount_of_fuel = int(input())
starting_amount_of_ammunition = int(input())
for commands in travel_route:
    parts = commands.split()
    command = parts[0]
    if command == "Travel":
        distance = int(parts[1])
        if starting_amount_of_fuel >= distance:
            starting_amount_of_fuel -= distance
            print(f"The spaceship travelled {distance} light-years.")
        else:
            print("Mission failed.")
            break
    elif command == "Enemy":
        armour_of_enemy = int(parts[1])
        if starting_amount_of_ammunition >= armour_of_enemy:
            starting_amount_of_ammunition -= armour_of_enemy
            print(f"An enemy with {armour_of_enemy} armour is defeated.")
        elif starting_amount_of_fuel >= armour_of_enemy * 2:
            starting_amount_of_fuel -= armour_of_enemy * 2
            print(f"An enemy with {armour_of_enemy} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break
    elif command == "Repair":
        added_number = int(parts[1])
        starting_amount_of_fuel += added_number
        starting_amount_of_ammunition += added_number * 2
        print(f"Ammunitions added: {added_number * 2}.")
        print(f"Fuel added: {added_number}.")
    elif command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break