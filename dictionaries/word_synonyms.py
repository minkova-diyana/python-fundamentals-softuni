count_of_words = int(input())
words_and_synonyms = {}
for count_word in range(count_of_words):
    word = input()
    synonym = input()
    if word not in words_and_synonyms:
        words_and_synonyms[word] = [synonym]
    else:
       words_and_synonyms[word].append(synonym)

for item in words_and_synonyms.items():
    print(f'{item[0]} - {", ".join(item[1])}')
