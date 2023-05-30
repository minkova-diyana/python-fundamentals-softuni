number_of_massages = int(input())
text = ''

for command in range(number_of_massages):
    curr_number = int(input())
    if curr_number == 88:
        text = 'Hello'
    elif curr_number == 86:
        text = 'How are you?'
    elif curr_number < 88:
        text = 'GREAT!'
    else:
        text = 'Bye.'
    print(text)
