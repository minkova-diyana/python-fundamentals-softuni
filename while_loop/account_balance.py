amount = input()

total = 0
while amount != 'NoMoreMoney':
    money = float(amount)
    if money < 0:
        print('Invalid operation!')
        break
    total += money
    amount = input()
    print(f'Increase: {money:.2f}')


print(f'Total: {total:.2f}')
