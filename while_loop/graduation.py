name_student = input()


years = 0
fail = 0

average = 0
while True:
    grate = float(input())
    years += 1

    if grate < 4.00:
        fail += 1
        if fail == 2:
            print(f'{name_student} has been excluded at {years} grade')
            break
        years -= 1
    else:
        average += grate

    if years == 12:
        final_grate = average / 12
        print(f'{name_student} graduated. Average grade: {final_grate:.2f}')
        break
