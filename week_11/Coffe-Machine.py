print("Welcome To Coffee Maker!")
menu =  {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk" : 0,
            "coffee": 20,
        },
        "price": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 150,
            "milk": 200,
            "coffee": 25,
        },
        "price": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 25,
        },
        "price": 3.0,
    }
}
n = 0
current_resource = {
    "ingredients": {
        "water": 500,
        "milk": 400,
        "coffee": 100
    },
    "money": 0
}
change = 0
def makeing_coffee():
    print("Welcome To Coffee Maker!")
    global final_sum
    current_resource["ingredients"]["water"] -=  menu[user_input]["ingredients"]["water"]
    current_resource["ingredients"]["milk"] -= menu[user_input]["ingredients"]["milk"]
    current_resource["ingredients"]["coffee"] -= menu[user_input]["ingredients"]["coffee"]

    print()
global make_coffee
def process_coins():
    print("insert a coin")
    quarters = 0.25
    dime = 0.10
    nickel = 0.05
    pennie = 0.01
    quarte = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_quarties = quarters*quarte
    total_dimes = dimes*dime
    total_nickels = nickels*nickel
    total_pennies = pennies*pennie
    print(f"quarters = {total_quarties}")
    print(f"dimes = {total_dimes}")
    print(f"nickels = {total_nickels}")
    print(f"pennies = {total_pennies}")
    final_sum = total_quarties + total_dimes + total_nickels + total_pennies
    print(f"final sum = {final_sum}")
    global change
    if user_input == "latte":
        if final_sum >= menu["latte"]["price"]:
            makeing_coffee()
        else:
            print("Sorry, you don't have enough money!")

    elif user_input == "espresso":
        print(change)
        if final_sum >= menu["espresso"]["price"]:
            makeing_coffee()
        else:
            print("Sorry, you don't have enough money!")

    elif user_input == "cappuccino":
        if final_sum >= menu["cappuccino"]["price"]:
            makeing_coffee()
        else:
            print("Sorry, you don't have enough money!")

    change += final_sum - menu[user_input]["price"]
    print(f"Change to {round(change, 2)}")





def report():
    global n

    for a , b in current_resource["ingredients"].items():
            print(f"{a} : {b}")
    print(f"money : {current_resource["money"]}")

    global make_coffee
    make_coffee = True

def sufficient_resource():
    short_input = menu[user_input]["ingredients"]
    if current_resource["ingredients"]["water"] >= short_input["water"] and current_resource["ingredients"]["milk"] >= short_input["milk"] and current_resource["ingredients"]["coffee"] >= short_input["coffee"]:
        process_coins()
    else:
        print("Sorry, you don't have enough")

make_coffee = True
while make_coffee:
    user_input = input("What would you like ?(espresso/latte/cappuccino):")
    if user_input == "report":
        report()
    elif user_input == "off":
        make_coffee = False
        print("Thank you for using Coffee Maker!")
    else:
        sufficient_resource()



