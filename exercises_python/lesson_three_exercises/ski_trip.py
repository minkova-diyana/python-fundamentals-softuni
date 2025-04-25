days = int(input())
room_kind = input()
grate = input()

nights = days - 1
total = 0
if room_kind == 'room for one person':
    total += nights * 18.00

elif room_kind == 'apartment':
    total += nights * 25.00
    if days < 10:
        total *= 0.70
    elif 10 <= days <= 15:
        total *= 0.65
    else:
        total *= 0.50

elif room_kind == 'president apartment':
    total += nights * 35.00
    if days < 10:
        total *= 0.90
    elif 10 <= days <= 15:
        total *= 0.85
    else:
        total *= 0.80


if grate == 'negative':
    total *= 0.90
elif grate == 'positive':
    total = (total * 0.25) + total


print(f'{total:.2f}')
