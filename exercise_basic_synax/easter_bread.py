budget = float(input())
price_per_kg_flour = float(input())
price_per_pack_eggs = price_per_kg_flour * 0.75
milk_per_liter = price_per_kg_flour * 1.25
#flour_needed_for_one_bread_kg = 1
#eggs_needed_for_one_bread_pack = 1
#needed_milk_for_bread = 0.250
money_left = budget
bread_count = 0
colored_eggs_count = 0
while True:
    one_bread_cost = price_per_pack_eggs + price_per_kg_flour + milk_per_liter / 4
    budget -= one_bread_cost
    if budget <= 0:
        break
    money_left -= one_bread_cost
    bread_count += 1
    colored_eggs_count += 3
    if bread_count % 3 == 0:
        colored_eggs_count -= bread_count - 2


print(f'You made {bread_count} loaves of Easter bread! Now you have {colored_eggs_count} eggs and'
      f' {money_left:.2f}BGN left.')
