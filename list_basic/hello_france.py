list_of_items_with_prices = input().split('|')
budget = float(input())
france_ticket_price = 150
profit = 0
new_prices_for_item = []

#item_conditions = {
#    'Clothes': 50.00,
#    'Shoes': 35.00,
#    'Accessories': 20.50
#}
for element in list_of_items_with_prices:
    item_and_price = element.split('->')
    type_of_item = item_and_price[0]
    price = float(item_and_price[1])
    if budget > price:
        if type_of_item == 'Clothes' and price <= 50:
            budget -= price
            new_price = price * 1.4
            profit += new_price - price
            new_prices_for_item.append(new_price)
        elif type_of_item == 'Shoes' and price <= 35:
            budget -= price
            new_price = price * 1.4
            profit += new_price - price
            new_prices_for_item.append(new_price)
        if type_of_item == 'Accessories' and price <= 20.50:
            budget -= price
            new_price = price * 1.4
            profit += new_price - price
            new_prices_for_item.append(new_price)

 #       if type_of_item in item_conditions and price <= item_conditions[type_of_item]:
 #           budget -= price
 #           new_price = price * 1.4
 #           profit += new_price - price
 #           new_prices_for_item.append(new_price)


print(' '.join([f'{new_prices_for_items:.2f}' for new_prices_for_items in new_prices_for_item]))
print(f'Profit: {profit:.2f}')
final_budget = budget + sum(new_prices_for_item)
if final_budget >= france_ticket_price:
    print('Hello, France!')
else:
    print('Not enough money.')

