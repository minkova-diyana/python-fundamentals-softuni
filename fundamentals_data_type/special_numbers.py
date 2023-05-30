number = int(input())


for count in range(1, number + 1):
    digits = count
    sum_digits = 0
    while digits > 0:
        sum_digits += digits % 10
        digits = int(digits / 10)

    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f'{count} -> True')
    else:
        print(f'{count} -> False')


