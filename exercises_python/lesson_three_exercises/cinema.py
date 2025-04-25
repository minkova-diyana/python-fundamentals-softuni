type_screening = input()
rows = int(input())
columns = int(input())

profit = 0
s_cinema = rows * columns

if type_screening == 'Premiere':
    profit = s_cinema * 12.00
elif type_screening == 'Normal':
    profit = s_cinema * 7.50
elif type_screening == 'Discount':
    profit = s_cinema * 5.00

print(f'{profit:.2f} leva')

