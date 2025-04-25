factor = int(input())
count = int(input())

multiples_list = [number * factor for number in range(1, count + 1)]
print(multiples_list)
#for number in range(1, count + 1):
    #multiples_list.append(number * factor)

#print(multiples_list)