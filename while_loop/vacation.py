vacation_budget = float(input())
startup_money = float(input())

days = 0
days_spend = 0

while True:
    days += 1
    money_movement = input()
    money = float(input())

    if money_movement == 'spend':
        days_spend += 1
        startup_money -= money
        if startup_money < 0:
            startup_money = 0
    elif money_movement == 'save':
        days_spend = 0
        startup_money += money

    if startup_money >= vacation_budget:
        print(f'You saved the money for {days} days.')
        break
    elif days_spend == 5:
        print("You can't save the money.")
        print(days)
        break
