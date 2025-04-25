failed_grades = int(input())

count = 0
average = 0
name = ''
failed = 0
name_exercise = input()
while name_exercise != 'Enough':
    grade = int(input())
    if grade <= 4:
        failed += 1
        if failed == failed_grades:
            print(f'You need a break, {failed} poor grades.')
            break

    count += 1
    average += grade
    name = name_exercise
    name_exercise = input()

if name_exercise == 'Enough':
    total = average / count
    print(f'Average score: {total:.2f}')
    print(f'Number of problems: {count}')
    print(f'Last problem: {name}')
