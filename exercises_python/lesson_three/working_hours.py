time_of_the_day = int(input())
day = input()

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday'\
        or day == 'Saturday':
    if time_of_the_day >= 10 and time_of_the_day <= 18:
        print("open")
    else:
        print('closed')

elif day == 'Sunday':
    print('closed')
