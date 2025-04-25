type_flower = input()
number_of_flowers = int(input())
budget = int(input())

price_for_one = 0
discount = 0

if type_flower == 'Roses':
    price_for_one = 5
    if number_of_flowers > 80:
        discount += 0.10
elif type_flower == 'Dahlias':
    price_for_one = 3.80
    if number_of_flowers > 90:
        discount += 0.15
elif type_flower == 'Tulips':
    price_for_one = 2.80
    if number_of_flowers > 80:
        discount += 0.15
elif type_flower == 'Narcissus':
    price_for_one = 3
    if number_of_flowers < 120:
        discount -= 0.15
elif type_flower == 'Gladiolus':
    price_for_one = 2.50
    if number_of_flowers < 80:
        discount -= 0.20

total_cost = number_of_flowers * price_for_one * (1 - discount)
diff = abs(total_cost - budget)

if budget >= total_cost:
    print(f'Hey, you have a great garden with {number_of_flowers} {type_flower} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
