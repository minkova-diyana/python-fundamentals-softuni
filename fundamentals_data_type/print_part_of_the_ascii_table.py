starting_char_index = int(input())
last_char_index = int(input())

for ascii_char in range(starting_char_index, last_char_index + 1):
    print(chr(ascii_char), end=' ')