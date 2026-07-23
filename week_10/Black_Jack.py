import random
def deal_card():
    cards = [11, 2 , 3, 4 ,5, 6, 7, 8, 9 , 10 , 10 , 10 , 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for i in range(2):
    new_card = deal_card()
    #user_cards += [new_card]
    user_cards.append(new_card)
user_card_sum = sum(user_cards)
print(f"Your cards: {user_cards}, current score: {user_card_sum} ")
computer_cards.append(deal_card())
#computer_cards = [deal_card()]
continuing = True
while continuing:
    print(f"computer's first card is : {computer_cards}")
    another_choice = input("Type 'Y' to get another card, type 'n' to pass: ").lower()


    if another_choice == 'y':
        choice = deal_card()
        user_cards.append(choice)
        user_card_sum = sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_card_sum}")

    #if user_card_sum >= 21:
        #print("You Loose")
        #continuing = False
    #computer_cards.append(deal_card())
    #print(f"Computers final hand: {computer_cards},final score: {sum(computer_cards)}")



