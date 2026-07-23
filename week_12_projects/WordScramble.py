#word scramble game
#computer selects a random word from a list ex:apple,banana,python,orange
#the computer scrambles the word and shows it
#example scrambled word : npaayb, user guesses banana,output correct or wrong the word was banana
#extra ask 5 words and keep score
"""Read Requirements
↓
Break into Steps
↓
Write Logic
↓
Code

This is exactly how real software development works.

Task 1: Word Scramble Game
Description

The computer selects a random word from a list.

Example:

apple
banana
python
orange

The computer scrambles the word and shows it.

Example:

Scrambled Word: npaayb

User guesses:

Enter your guess: banana

Output:

Correct!

or

Wrong!
The word was banana
Extra

Ask 5 words and keep score.

Final output:

Score: 4/5"""

import random
from random import shuffle

print(".............Welcome To Scramble Game.........")
list_of_words = ["apple","banana","python","orange"]
word = random.choice(list_of_words)

computer_choice = []
shuffled_words = ""
for letter in word:
    computer_choice += letter

random.shuffle(computer_choice)
shuffled_words = ''.join(computer_choice)

print(shuffled_words)
game_over = False
lives = 5

while not game_over:
        guess_word = input("Enter your guess:")
        if guess_word == word:
            print("correct!",guess_word)
            game_over = True
        else:
            print("incorrect!")
            print("the word was ",word)
            lives -=1
        if lives == 0:
            game_over = True
            print("You Lost")











