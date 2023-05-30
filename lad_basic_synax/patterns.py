number_for_pattern = int(input())

for i in range(1, number_for_pattern + 1):
    for j in range(i):
        print('*', end='')
    print()
for i in reversed(range(1, number_for_pattern)):
    for j in range(i):
        print('*', end='')
    print()
