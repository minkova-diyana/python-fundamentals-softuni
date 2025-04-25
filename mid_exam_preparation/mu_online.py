dungeon_rooms = input().split('|')
health = 100
healing = 0
bitcoin = 0
command = ''
digit = 0
you_not_dead = True
rooms = 0
for separation in dungeon_rooms:
    rooms += 1
    command_digits = separation.split()
    command = command_digits[0]
    digit = int(command_digits[1])
    current_health = health
    if command == 'potion':
        health += digit
        if health > 100:
            health = 100
        healing = abs(health - current_health)
        print(f'You healed for {healing} hp.')
        print(f'Current health: {health} hp.')

    elif command == 'chest':
        bitcoin += digit
        print(f'You found {digit} bitcoins.')
    else:
        health -= digit
        if health > 0:
            print(f'You slayed {command}.')
        else:
            you_not_dead = False
            print(f'You died! Killed by {command}.')
            print(f'Best room: {rooms}')
            break
if you_not_dead:
    print('You\'ve made it!')
    print(f'Bitcoins: {bitcoin}')
    print(f'Health: {health}')


