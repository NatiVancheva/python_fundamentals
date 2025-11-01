days_of_adventure = int(input())
number_of_participants = int(input())
initial_energy = float(input())
water_per_person_per_day = float(input())
food_per_person_per_day = float(input())
total_water = days_of_adventure * number_of_participants * water_per_person_per_day
total_food = days_of_adventure * number_of_participants * food_per_person_per_day
for day in range(1, days_of_adventure + 1):
    energy_loss = float(input())
    initial_energy -= energy_loss
    if initial_energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break
    if day % 2 == 0:
        initial_energy *= 1.05
        total_water *= 0.7
    if day % 3 == 0:
        initial_energy *= 1.1
        total_food -= total_food / number_of_participants

else:
    print(f"You are ready for the quest. You will be left with {initial_energy:.2f} energy!")

