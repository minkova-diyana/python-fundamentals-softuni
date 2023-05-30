lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_cost = 0
shield_count = 0
helmet_count = 0
sword_count = 0

armor_count = 0
for count in range(1, lost_fights + 1):
    if count % 2 == 0:
        total_cost += helmet_price
    if count % 3 ==0:
        total_cost += sword_price
    if count % 2 == 0 and count % 3 ==0:
        total_cost += shield_price
        shield_count += 1
        if shield_count % 2 == 0:
            total_cost += armor_price

print(f'Gladiator expenses: {total_cost:.2f} aureus')
