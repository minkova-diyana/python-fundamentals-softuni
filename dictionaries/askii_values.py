characters = input().split(', ')
ascii_dic = {characters[index]: ord(characters[index]) for index in range(len(characters))}
print(ascii_dic)
