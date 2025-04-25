n = int(input())
count = 0
for x in range(n + 1):
    for y in range(n + 1):
        for z in range(n + 1):
            if x + y + z == n:
                count += 1
print(count)
