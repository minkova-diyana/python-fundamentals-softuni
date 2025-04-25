list_of_things = []
while True:
    sequence = input()
    if sequence == 'stop':
        break
    list_of_things.append(sequence)

resources = {}
for index in range(0,len(list_of_things), 2):
    key = list_of_things[index]
    if key not in resources:
        resources[key] = int(list_of_things[index + 1])
    else:
        resources[key] += int(list_of_things[index + 1])

for resource, quantity in resources.items():
    print(f'{resource} -> {quantity}')

