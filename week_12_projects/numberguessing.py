""""Number Guessing Game (Advanced)
Description

Computer chooses a random number between 1 and 100.

User chooses difficulty:

Easy
Hard

Easy:

10 attempts

Hard:

5 attempts

Output:

Too High

or

Too Low

or

You Won

If attempts finish:

You Lost
The Number Was 57"""
import random
computer_choice = random.randint(1, 100)
print(computer_choice)
lives = 10

game_over = False
valid_choice = False
while not valid_choice:
    user_choice = input("Select user choice:Hard or Easy:").lower()
    if user_choice != "hard" and user_choice != "easy":
        print("Enter valid choice that is 'hard' or 'easy'")
    else:
        while not game_over:
            select_number = int(input("from 1 to 100 any number:"))
            if user_choice == "hard":
                if select_number > computer_choice:
                    print("Too High")
                    lives -= 2
                    if lives == 0:
                        print("You Lost")
                        game_over = True
                elif select_number < computer_choice:
                    print("Too Low")
                    lives -= 2
                    if lives == 0:
                        print("You Lost")
                        game_over = True
                else:
                    print("You Won")
                    game_over = True
                print("you have lives:", lives)
            else:
                if user_choice == "easy":
                    if select_number > computer_choice:
                        print("Too High")
                        lives -= 1
                        if lives == 0:
                            print("You Lost")
                            game_over = True

                    elif select_number < computer_choice:
                        print("Too Low")
                        lives -= 1
                        if lives == 0:
                            print("You Lost")
                            game_over = True
                    else:
                        print("You Won")
                        game_over = True
                    print("you have lives:", lives)
        valid_choice = True






