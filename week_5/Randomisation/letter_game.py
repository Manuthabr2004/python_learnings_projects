import random
print("............Welcome to Letter Game............!")
guess = input("Guess a letter: ").lower()
letter = "abcdefghijklmnopqrstuvwxyz"
random = random.choice(letter)
print(random)

if guess == random:
    print("Guess The Letter")
    print(".........You Won.......")
else:
    print(".......You Lose.......")