width_space = int(input())
length_space = int(input())
h_space = int(input())

free_space = width_space * length_space * h_space
filled_space = 0

boxes = input()
while boxes != 'Done':
    filled_space += int(boxes)
    if filled_space >= free_space:
        print(f'No more free space! You need {abs(free_space - filled_space)} Cubic meters more.')
        break
    boxes = input()

if boxes == 'Done':
    print(f'{abs(free_space - filled_space)} Cubic meters left.')
    