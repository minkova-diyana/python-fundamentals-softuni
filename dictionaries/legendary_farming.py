items_to_win = {'shards': 0, 'fragments': 0, 'motes': 0}
legendary_item = ''
game_won = False
while True:
    list_with_items = input().lower().split()
    for index in range(0, len(list_with_items), 2):
        key, value = list_with_items[index + 1], int(list_with_items[index])
        if key not in items_to_win:
            items_to_win[key] = 0
        items_to_win[key] += value
        if items_to_win['shards'] >= 250:
            game_won = True
            items_to_win['shards'] -= 250
            legendary_item = 'Shadowmourne'
            break
        elif items_to_win['fragments'] >= 250:
            game_won = True
            items_to_win['fragments'] -= 250
            legendary_item = 'Valanyr'
            break
        elif items_to_win['motes'] >= 250:
            game_won = True
            items_to_win['motes'] -= 250
            legendary_item = 'Dragonwrath'
            break
    if game_won:
        break
print(f'{legendary_item} obtained!')
for material, quantity in items_to_win.items():
    print(f'{material}: {quantity}')

