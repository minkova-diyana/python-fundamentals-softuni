import math

number_of_people = int(input())
capacity_of_elevator = int(input())
curses_of_the_elevator = math.ceil(number_of_people / capacity_of_elevator)
if curses_of_the_elevator == 1:
    print('All the persons fit inside the elevator.')
    print('Only one course is needed.')
else:
    print(curses_of_the_elevator)
