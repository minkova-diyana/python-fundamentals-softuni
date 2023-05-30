budget = int(input())
command = input()
total_cost = 0
while command != 'End':
    total_cost += int(command)
    if total_cost > budget:
        print('You went in overdraft!')
        break
    command = input()

if command == 'End':
    print('You bought everything needed.')
