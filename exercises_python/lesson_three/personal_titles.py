age = float(input())
gander = input()

if gander == 'm':
    if age >= 16:
        print('Mr.')
    else:
        print('Master')

elif gander == 'f':
    if age >= 16:
        print('Ms.')
    else:
        print('Miss')

