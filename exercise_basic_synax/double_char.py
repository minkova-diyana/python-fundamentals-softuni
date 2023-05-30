text = input()

while text != 'End':
    if text != 'SoftUni':
        new_text = ''
        for char in text:
            new_text += char * 2
        print(new_text)
    text = input()
