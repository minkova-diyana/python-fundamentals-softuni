beginning = int(input())
end = int(input())
magic_num = int(input())
FALSE_DATA = False
count = 0
sum_num = 0
i = 0
y = 0
for i in range(beginning, end + 1):
    for y in range(beginning, end + 1):
        count += 1
        sum_num = i + y
        if sum_num == magic_num:
            FALSE_DATA = True
        else:
            FALSE_DATA = False
            break
    if sum_num == magic_num:
        FALSE_DATA = True
    else:
        FALSE_DATA = False
        break

if FALSE_DATA != 'False':
    print(f'Combination N:{count} ({i} + {y} = {magic_num})')
else:
    print(f'{count} combinations - neither equals {magic_num}')
