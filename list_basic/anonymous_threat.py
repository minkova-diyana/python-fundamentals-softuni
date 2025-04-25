def merge_command(line, given_command):
    starting_index, end_index = int(given_command[1]), int(given_command[2])
    concatenated_words = []
    for index in reversed(range(len(line))):
        if starting_index <= index <= end_index:
            concatenated_words.append(line[index])
            line.pop(index)
    concatenated_words = concatenated_words[::-1]
    word = ''.join(concatenated_words)
    line.insert(starting_index, word)
    return line


def divide_command(line, given_command):
    given_index, partitions = int(given_command[1]), int(given_command[2])
    divided_words = ''
    word = line[given_index]
    slicing_step = len(word) // partitions
    count = 0
    for char in word:
        count += 1
        divided_words += char
        if count == slicing_step:
            divided_words += ' '
            count = 0
    line.pop(given_index)
    line.insert(given_index, divided_words)
    return line


line_to_analyze = input().split()
analyzed_line = line_to_analyze.copy()

while True:
    commands = input().split()
    command = commands[0]
    if command == '3:1':
        break
    if command == 'merge':
        analyzed_line = merge_command(analyzed_line, commands)
    elif command == 'divide':
        analyzed_line = divide_command(analyzed_line, commands)

print(' '.join(analyzed_line))
