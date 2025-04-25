type_of_fire = input().split('#')
given_watter = int(input())
total_fire = 0
print('Cells:')
for element in type_of_fire:
    parameters = element.split(' = ')
    cell = parameters[0]
    fire = int(parameters[1])
    if given_watter < fire:
        continue
    if cell == 'High' and 81 <= fire <= 125:
        given_watter -= fire
        total_fire += fire
        print(f'- {fire}')
    elif cell == 'Medium' and 51 <= fire <= 80:
        given_watter -= fire
        total_fire += fire
        print(f'- {fire}')
    elif cell == 'Low' and 1 <= fire <= 50:
        given_watter -= fire
        total_fire += fire
        print(f'- {fire}')
print(f'Effort: {total_fire * 0.25:.2f}')
print(f'Total Fire: {total_fire}')

