gifts = input().split()
command = input()
while command != 'No Money':
    list_command = command.split()
    task = list_command[0]
    gift = list_command[1]
    if task == 'OutOfStock':
        for element in range(len(gifts)):
           if gifts[element] == gift:
               gifts[element] = 'None'
    elif task == 'Required':
        index = list_command[2]
        if len(gifts) > int(index) >= 0:
            gifts[int(index)] = gift
    elif task == 'JustInCase':
        gifts[-1] = gift

    command = input()
gifts = [gift for gift in gifts if gift != 'None']
print(' '.join(gifts))


