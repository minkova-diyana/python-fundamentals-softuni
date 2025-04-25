budged = int(input())
season = input()
fishermen = int(input())

price = 0
discount = 0
total_price = 0

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600


if fishermen <= 6:
    price *= 0.90
elif fishermen >= 12:
    price *= 0.75
else:
    price *= 0.85

if fishermen % 2 == 0 and season != 'Autumn':
    discount = 0.95
    total_price = price * discount
else:
    total_price = price
diff = abs(budged - total_price)

if budged >= total_price:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')

