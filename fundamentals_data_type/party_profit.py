group_size = int(input())
days = int(input())
coins = 0

for adventure in range(1, days + 1):
    if adventure % 10 == 0:
        group_size -= 2
    if adventure % 15 == 0:
        group_size += 5
    if adventure % 3 == 0:
        coins -= 3 * group_size
    if adventure % 5 == 0:
        coins += 20 * group_size
        if adventure % 3 == 0:
            coins -= 2 * group_size
    coins += 50 - 2 * group_size

print(f'{group_size} companions received {coins // group_size} coins each.')