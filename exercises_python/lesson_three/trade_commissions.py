city = input()
volume = float(input())

FALSE_DATA = False

if city == 'Sofia':
    if 0 <= volume <= 500:
        volume *= 0.05
    elif 500 < volume <= 1000:
        volume *= 0.07
    elif 1000 < volume <= 10000:
        volume *= 0.08
    elif volume > 10000:
        volume *= 0.12
    else: FALSE_DATA = True
elif city == 'Varna':
    if 0 <= volume <= 500:
        volume *= 0.045
    elif 500 < volume <= 1000:
        volume *= 0.075
    elif 1000 < volume <= 10000:
        volume *= 0.10
    elif volume > 10000:
        volume *= 0.13
    else:
        FALSE_DATA = True
elif city == 'Plovdiv':
    if 0 <= volume <= 500:
        volume *= 0.055
    elif 500 < volume <= 1000:
        volume *= 0.08
    elif 1000 < volume <= 10000:
        volume *= 0.12
    elif volume > 10000:
        volume *= 0.145
    else:
        FALSE_DATA = True
else:
    FALSE_DATA = True

if not FALSE_DATA:
    print(f'{volume:.2f}')
else:
    print('error')
