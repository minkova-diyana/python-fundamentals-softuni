hours_exam = int(input())
min_exam = int(input())
hours_arrive = int(input())
min_arrive = int(input())

minutes_exam = hours_exam * 60 + min_exam
minutes_arrive = hours_arrive * 60 + min_arrive

diff = minutes_exam - minutes_arrive
hours = 0
minutes = 0
abs_diff = 0
if minutes_exam == minutes_arrive:
    print('On time')

elif 0 < diff <= 30:
    print('On time')
    print(f'{diff} minutes before the start')

elif minutes_exam > minutes_arrive and diff > 30:
    if diff > 59:
        hours = diff // 60
        minutes = diff % 60

        print('Early')
        if minutes < 10:
            print(f'{hours}:0{minutes} hours before the start')
        else:
            print(f'{hours}:{minutes} hours before the start')
    else:
        print('Early')
        print(f'{diff} minutes before the start')

elif minutes_exam < minutes_arrive:
    abs_diff = abs(diff)
    if abs_diff <= 59:
        print('Late')
        print(f'{abs_diff} minutes after the start')
    else:
        hours = abs_diff // 60
        minutes = abs_diff % 60
        print('Late')
        if minutes < 10:
            print(f'{hours}:0{minutes:} hours after the start')
        else:
            print(f'{hours}:{minutes:} hours after the start')





