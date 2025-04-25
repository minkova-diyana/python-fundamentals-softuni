month = input()
number_nights = int(input())

studio = 0
apartment = 0

discount_apartments = 0.90

if month == 'May' or month == 'October':
    studio = number_nights * 50
    apartment = number_nights * 65
    if 14 > number_nights > 7:
        studio *= 0.95

    elif number_nights > 14:
        studio *= 0.70

elif month == 'June' or month == 'September':
    studio = number_nights * 75.20
    apartment = number_nights * 68.70
    if number_nights > 14:
        studio *= 0.80

elif month == 'July' or month == 'August':
    studio = number_nights * 76
    apartment = number_nights * 77

if number_nights > 14:
    apartment *= discount_apartments

print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')
