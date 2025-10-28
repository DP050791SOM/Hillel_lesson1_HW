import string
ht=str("Введите строку для преобразования в хештег:")
print(ht)

user_input = input("")

hashtag = "#" + "".join(word.capitalize()
for word in user_input.translate(
    str.maketrans('', '', string.punctuation)
    ).split())[:140]

print(hashtag)
exit()