number_of_times_filling_the_tank = int(input())
water_tank_capacity_liters = 255
total_water_in_the_tank = 0
overflow_liters = 0
for liters in range(number_of_times_filling_the_tank):
    liters_poured = int(input())
    water_tank_capacity_liters += overflow_liters
    if water_tank_capacity_liters < liters_poured:
        overflow_liters += liters_poured
        print('Insufficient capacity!')
    water_tank_capacity_liters -= liters_poured
    total_water_in_the_tank += liters_poured

print(total_water_in_the_tank - overflow_liters)

