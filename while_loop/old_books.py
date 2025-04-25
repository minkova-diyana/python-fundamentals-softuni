target_book = input()

count = 0
books = input()
while books != 'No More Books':

    if books == target_book:
        print(f'You checked {count} books and found it.')
        break
    count += 1
    books = input()

if books == 'No More Books':
    print('The book you search is not here!')
    print(f'You checked {count} books.')
