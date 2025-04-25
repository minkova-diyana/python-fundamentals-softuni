
journal = input().split(', ')
command = input()

while command != 'Craft!':

    command = command.split(' - ')
    left_side = command[0]
    right_side = command[1]

    if left_side == 'Collect':
        if right_side in journal:
            continue
        else:
            journal.append(right_side)
    elif left_side == 'Drop':
        if right_side in journal:
            journal.remove(right_side)
    elif left_side == 'Combine Items':
        right_side = right_side.split(':')
        old_item = right_side[0]
        new_item = right_side[1]
        if old_item in journal:
            index = journal.index(old_item)
            journal.insert(index + 1, new_item)
    elif left_side == 'Renew':
        if right_side in journal:
            element_index = journal.index(right_side)
            element = journal.pop(element_index)
            journal.append(right_side)
    command = input()

print(', '.join(journal))
