from sys import maxsize
num = input()

min_num = - maxsize
min = 0

while num != 'Stop':
    min = int(num)
    if min > min_num:
        min_num = min

    num = input()
print(min_num)
