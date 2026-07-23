import random
print("...........Welcome to the Rock Paper Scissor Game............!" )

set = ['rock' , 'paper' , 'scissor']
print(set)
random = random.choice(set)
computer_choice = random
user_choice = input(" Please choose your option: Type 'rock' or 'paper' or 'scissor' ").lower()
print(f"user choice is {user_choice}")
print(f"computer choice is {computer_choice}")
if user_choice == 'rock' and computer_choice == set[1]:
    print("You Win!")
elif user_choice == 'rock' and computer_choice == set[2]     :
    print("You Loose")
elif user_choice == 'paper' and computer_choice == set[0]:
    print("You Win")
elif user_choice == 'paper' and computer_choice == set[2]:
    print("You Loose")
elif user_choice == 'scissor' and computer_choice == set[0]:
    print("You Loose")
elif user_choice == 'scissor' and computer_choice == set[1]:
    print("you Win")
elif user_choice == computer_choice:
    print("DRAW")
else:
    print("Invalid Choice please try again with valid choices")


