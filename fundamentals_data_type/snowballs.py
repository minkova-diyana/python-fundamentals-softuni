from sys import maxsize
quantity_snowballs = int(input())
value_of_snowball = 0
best_value = - maxsize
best_weight = 0
best_time = 0
best_quality = 0
for snowball in range(quantity_snowballs):
    weight_snowball = int(input())
    time_of_snowball = int(input())
    quality_of_snowball = int(input())
    value_of_snowball = (weight_snowball // time_of_snowball) ** quality_of_snowball
    if value_of_snowball > best_value:
        best_value = value_of_snowball
        best_weight = weight_snowball
        best_time = time_of_snowball
        best_quality = quality_of_snowball

print(f'{best_weight} : {best_time} = {best_value} ({best_quality})')


