n = int(input())

even_num = 0
odd_num = 0

for i in range(n):
    curr_num = int(input())
    if i % 2 == 0:
        even_num += curr_num
    else:
        odd_num += curr_num

if even_num == odd_num:
    print('Yes')
    print(f'Sum = {even_num} ')
else:
    print('No')
    print(f'Diff = {abs(even_num - odd_num)}')
