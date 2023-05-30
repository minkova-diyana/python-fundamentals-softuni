num_of_orders = int(input())

price_order = 0
total_cost = 0

for order in range(num_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue
    price_order = price_per_capsule * capsules_needed_per_day * days
    total_cost += price_order
    print(f'The price for the coffee is: ${price_order:.2f}')

print(f'Total: ${total_cost:.2f}')