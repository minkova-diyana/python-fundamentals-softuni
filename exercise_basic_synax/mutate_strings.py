given_string_one = input()
given_string_two = input()

old_word = given_string_one
for char in range(len(given_string_two)):
    left_side = given_string_two[:char + 1]
    right_side = given_string_one[char + 1:]
    new_word = left_side + right_side
    if new_word == old_word:
        continue
    old_word = new_word
    print(new_word)
