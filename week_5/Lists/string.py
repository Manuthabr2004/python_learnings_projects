import random
word = "apple"
list = []
for letter in word:
    list.append(letter)
    print(letter)
print(list)
random.shuffle(list)
print(list)
characters = ""
for item in list:
    characters += item
print(characters)

