fruit = input().lower()
day = input()
quantity = float(input())

FALSE_DATA = False

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        quantity *= 2.50
    elif fruit == 'apple':
        quantity *= 1.20
    elif fruit == 'orange':
        quantity *= 0.85
    elif fruit == 'grapefruit':
        quantity *= 1.45
    elif fruit == 'kiwi':
        quantity *= 2.70
    elif fruit == 'pineapple':
        quantity *= 5.50
    elif fruit == 'grapes':
        quantity *= 3.85
    else:
        FALSE_DATA = True
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        quantity *= 2.70
    elif fruit == 'apple':
        quantity *= 1.25
    elif fruit == 'orange':
        quantity *= 0.90
    elif fruit == 'grapefruit':
        quantity *= 1.60
    elif fruit == 'kiwi':
        quantity *= 3.00
    elif fruit == 'pineapple':
        quantity *= 5.60
    elif fruit == 'grapes':
        quantity *= 4.20

else:
    FALSE_DATA = True

if not FALSE_DATA:
    print(f'{quantity:.2f}')
else:
    print('error')
