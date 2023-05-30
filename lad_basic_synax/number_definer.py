num = float(input())

#type_num = ''
#kind = ''
#if num == 0:
   #print('zero')
#elif num > 0:
    #type_num = 'positive'
#else:
    #type_num = 'negative'

#if abs(num) < 1 and abs(num) != 0:
    #kind = 'small'
#elif abs(num) > 1000000:
    #kind = 'large'

#print(f'{kind} {type_num}')

if num == 0:
    print('zero')
elif num > 0:
    if num < 1:
        print('small positive')
    elif num > 1000000:
        print('large positive')
    else:
        print('positive')
else:
    if abs(num) < 1:
        print('small negative')
    elif abs(num) > 1000000:
        print('large negative')
    else:
        print('negative')

