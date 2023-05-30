name = input()
FALSE_DATA = False
while name != 'Welcome!':
    if name == 'Voldemort':
        FALSE_DATA = True
        break
    elif len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()

if FALSE_DATA:
    print('You must not speak of that name!')
else:
    print('Welcome to Hogwarts.')
