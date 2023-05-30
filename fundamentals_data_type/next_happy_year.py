given_year = int(input())

while True:
    given_year += 1
    new_happy_year = str(given_year)
    if len(set(new_happy_year)) == len(new_happy_year):
        break


print(new_happy_year)