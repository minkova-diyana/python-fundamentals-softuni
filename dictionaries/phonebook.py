count = 0
phone_book = {}
while True:
    person_info = input()
    if '-' not in person_info:
        count = int(person_info)
        break
    person_number = person_info.split('-')
    phone_book[person_number[0]] = person_number[1]
for names in range(count):
    name = input()
    if name in phone_book:
        print(f'{name} -> {phone_book[name]}')
    else:
        print(f'Contact {name} does not exist.')

