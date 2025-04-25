country_list = input().split(', ')
capital_list = input().split(', ')
country_capital = {country_list[index]: capital_list[index] for index in range(len(country_list))}

for country, capital in country_capital.items():
    print(f'{country} -> {capital}')

