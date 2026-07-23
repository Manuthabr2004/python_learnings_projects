#1.should be 6 chances
#list of word
#random choice of any item in list
#print blanks of how many letters in a word
#letters in guess == letter in randomchoice item then print that index letter remaining should be blank
import random
list = ["apple","banana","carrot","fruit","baloon","face","zebra","language",'happy']
computer_choice = random.choice(list)
print(computer_choice)


guessed_letters = []

lives = 6
while lives >0:
    guess_letter = input("Guess letters?:")

    if guess_letter in guessed_letters:
        print("You already guessd that letter")
        continue
    guessed_letters.append(guess_letter)

    display = ""

    for letter in computer_choice:
        if letter in guess_letter:
            display += letter
        else:
            display += "_"
    print(display)

    if guess_letter not in computer_choice:
        lives -= 1
        print("wrong guess")






