list_of_numbers = [int(n) for n in input().split(', ')]
groups_interval = 10

while list_of_numbers:
    separated_list = []
    for num in list_of_numbers:
        if num <= groups_interval:
            separated_list.append(num)
    print(f"Group of {groups_interval}'s: {separated_list}")
    list_of_numbers = [number for number in list_of_numbers if number not in separated_list]
    groups_interval += 10
