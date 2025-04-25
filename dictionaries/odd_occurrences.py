words = input().lower().split()
dic_words = {}
for word in words:
    if word not in dic_words:
        dic_words[word] = 1
    else:
        dic_words[word] += 1

for item in dic_words.items():
    if item[1] % 2 != 0:
        print(item[0], end=' ')
