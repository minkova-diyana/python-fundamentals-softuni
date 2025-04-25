list_of_items_with_prices = input().split('|')
budget = float(input())
france_ticket_price = 150
profit = 0
final_budget = 0
new_prices_for_item = []

# Define the conditions and limits for each type of item
item_conditions = {
    'Clothes': 50.00,
    'Shoes': 35.00,
    'Accessories': 20.50
}

for element in list_of_items_with_prices:
    item_and_price = element.split('->')
    type_of_item = item_and_price[0]
    price = float(item_and_price[1])

    if budget < price:
        continue

    if type_of_item in item_conditions and price <= item_conditions[type_of_item]:
        budget -= price
        profit += price
        new_price = round(price * 0.4 + price, 2)
        final_budget += new_price
        new_prices_for_item.append(new_price)

new_prices_for_item = [str(ele) for ele in new_prices_for_item]
profit = round(profit * 0.4, 2)

print(' '.join(new_prices_for_item))
print(f'Profit: {profit}')

if final_budget + budget >= france_ticket_price:
    print('Hello, France!')
else:
    print('Not enough money.')
