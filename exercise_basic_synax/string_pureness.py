number_of_string = int(input())

char_text = ''
for count in range(number_of_string):
    text = input()
    for i in range(len(text)):
        char_text = text[i]
        if char_text == ',' or char_text == '.' or char_text == '_':
            print(f"{text} is not pure!")
            break
        else:
            print(f"{text} is pure.")