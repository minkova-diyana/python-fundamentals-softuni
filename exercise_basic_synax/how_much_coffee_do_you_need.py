command = input()

cups_of_coffee = 0
while command != 'END':
    if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
        cups_of_coffee += 1
    elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
        cups_of_coffee += 2

    command = input()
if cups_of_coffee > 5:
    print('You need extra sleep')
else:
    print(cups_of_coffee)
