def changed_words(ciphered_word):
    deciphered_words = []
    for word in ciphered_word:
        digits = []
        letters = []
        for character in word:
            if character.isdigit():
                digits.append(character)
            else:
                letters.append(character)
        first_letter = chr(int(''.join(map(str, digits))))
        letters[0], letters[-1] = letters[-1], letters[0]
        letters.insert(0, first_letter)
        new_word = ''.join(letters)
        deciphered_words.append(new_word)
    return deciphered_words


code_word = input().split()
cracked_code = changed_words(code_word)
print(' '.join(cracked_code))
