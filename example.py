text = input().split()

while True:

    command = input()
    if command == '3:1':
        print(*text)
        break

    command = command.split()

    if command[0] == 'merge':
        start_index = int(command[1])
        end_index = int(command[2]) + 1

        if start_index >= len(text) or end_index <= 0:
            continue

        if start_index > end_index:
            continue

        if start_index < 0:
            start_index = 0

        if end_index >= len(text):
            end_index = len(text)

        result = "".join((text[start_index:end_index]))

        del text[start_index:end_index]
        text.insert(start_index, result)

    if command[0] == 'divide':
        split_index = int(command[1])
        split_count = int(command[2])
        division = text[split_index]
        partitions = len(division) // split_count
        if split_index not in range(len(text)):
            continue

        curr_string = ""

        counter = 0
        still_counter = 0
        for el in division:
            if still_counter == split_count - 1:
                curr_string += el
            else:
                counter += 1
                curr_string += el

                if counter == partitions:
                    curr_string += " "
                    counter = 0
                    still_counter += 1

        del text[split_index]
        text.insert(split_index, curr_string)