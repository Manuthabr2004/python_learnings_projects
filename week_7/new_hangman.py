#print welcome to hangman
#create a list containg words
#create input for guess word
#create random to choose random word in list
#create display
#create lives as hangman has 6 lives
#create a for loop take each letter compare with guess letter its correct print letter store it in variable if not equal append blank to current word and create a list to store guessed word and print already guessed and deduct 1 lives
#if no blank in the word its filled then you win if 6 lives over not filled game over
import random
print("............Welcome To Hangman Game!...........")
list = ["apple","banana","carrot","fruit","baloon","face","zebra","language",'happy']
computer_choice = random.choice(list)
print(computer_choice)
length = len(computer_choice)
word_len = " "
for i in range(length):
    word_len += "_"
print(word_len)


lives = 6
already_guessed = []
game_over = False
while not game_over:
    display = " "
    guess_letter = input("Guess a letter:").lower()
    if guess_letter in already_guessed:
        print("You already guessed")
    else:
        already_guessed.append(guess_letter)
        for letter in computer_choice:

            if guess_letter == letter:
                display += letter
            elif letter in already_guessed:
                display += letter
            else:
                display += "_"

        print(display)
        if guess_letter not in computer_choice:
            lives -= 1
            if lives == 0:
                game_over = True
                print("You lose!")
        print(lives)


        if "_" not in display:
            game_over = True
            print("You win")




