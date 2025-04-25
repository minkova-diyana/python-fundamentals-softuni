width = int(input())
length = int(input())

cake = width * length

pieces = input()
while pieces != 'STOP':
    cake -= int(pieces)
    if cake <= 0:
        print(f'No more cake left! You need {abs(cake)} pieces more.')
        break

    pieces = input()
if pieces == 'STOP':
    print(f'{cake} pieces are left.')
