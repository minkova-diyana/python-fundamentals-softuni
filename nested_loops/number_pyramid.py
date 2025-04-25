n = int(input())

counter = 0
FALSE_DATA = False

for row in range(1, n + 1):
    for col in range(1, row +1):
        counter += 1
        if counter > n:
            FALSE_DATA = True
            break
        print(str(counter) + ' ', end='')
    if FALSE_DATA:
        break
    print()
