first_employee_capacity = int(input())
second_employee_capacity = int(input())
third_employee_capacity = int(input())
number_of_students = int(input())
total_time_in_hours = 0
total_capacity_per_hour = first_employee_capacity + second_employee_capacity + third_employee_capacity
while number_of_students > 0:
    total_capacity_per_hour += 1
    if total_time_in_hours % 4 == 0:
        continue
    number_of_students -= total_capacity_per_hour
print(f"Time needed: {total_time_in_hours}h.")
