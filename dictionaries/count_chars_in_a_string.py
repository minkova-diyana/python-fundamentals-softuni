text = input()
letters_count = {}

for letter in text:
    if letter not in letters_count:
        letters_count[letter] = 1
    else:
        letters_count[letter] += 1

for item in letters_count.items():
    if item[0] != ' ':
        print(f'{item[0]} -> {item[1]}')

