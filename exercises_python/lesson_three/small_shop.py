product = input()
city = input()
items = float(input())
total_bil = 0


if city == "Sofia":
    if product == 'coffee':
        total_bil = items * 0.50
    elif product == 'water':
        total_bil = items * 0.80
    elif product == 'beer':
        total_bil = items * 1.20
    elif product == 'sweets':
        total_bil = items * 1.45
    elif product == 'peanuts':
        total_bil = items * 1.60
elif city == "Plovdiv":
    if product == 'coffee':
        total_bil = items * 0.40
    elif product == 'water':
        total_bil = items * 0.70
    elif product == 'beer':
        total_bil = items * 1.15
    elif product == 'sweets':
        total_bil = items * 1.30
    elif product == 'peanuts':
        total_bil = items * 1.50
elif city == "Varna":
    if product == 'coffee':
        total_bil = items * 0.45
    elif product == 'water':
        total_bil = items * 0.70
    elif product == 'beer':
        total_bil = items * 1.10
    elif product == 'sweets':
        total_bil = items * 1.35
    elif product == 'peanuts':
        total_bil = items * 1.55

print(total_bil)
