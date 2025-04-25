change = float(input())


coins = 0
while change > 0:
    coins += 1

    if change >= 2:
        change -= 2
    elif 2 > change >= 1:
        change -= 1
    elif 1 > change >= 0.50:
        change -= 0.50
    elif 0.50 > change >= 0.20:
        change -= 0.20
    elif 0.20 > change >= 0.10:
        change -= 0.10
    elif 0.10 > change >= 0.05:
        change -= 0.05
    elif 0.05 > change >= 0.02:
        change -= 0.02
    elif 0.02 > change >= 0.01:
        change -= 0.01

change = round(change, 2)

print(coins)
