print("........Welcome to Treasure Island Game......!")
print("--------Your mission is to find a treasure------")
choice1 = input("You/'r at a crossrod where the island is there here where you want to go"
                   " 'Type Left' or 'Right'.").lower()
if choice1 == 'left':
    print("Do You want to swim or wait? .")
    choice2 = input("Enter 'Swim' or 'Wait'.").lower()
    if choice2 == 'wait':
        print("Which door do you want to open 'Blue door','Red' or 'yellow'.")
        choice3 = input("Enter 'Blue' or 'Yellow' or 'Red'.").lower()
        if choice3 == 'red':
            print(".......Game Over.......!")
        elif choice3 == 'yellow':
            print('........You Win The Game.......')
        else:
            print(".......Game Over.......!")
    else:
        print(".......Game Over.......!")
else:
    print(".......Game Over.......!")


