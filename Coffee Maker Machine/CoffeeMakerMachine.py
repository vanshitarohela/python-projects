def check_requirements(input, MENU, resources):
    """Returns True if requirements are met. Else returns string specifying which resource is insufficient."""
    if MENU[input]['water'] > resources['water']:
        return "Sorry! We have run out of water."
     
    elif MENU[input]['milk'] > resources['milk']:
        return "Sorry! We have run out of milk."

    elif MENU[input]['coffee'] > resources['coffee']:
        return "Sorry! We have run out of coffee."

    return True


def user_money():
    """Calculates the user's money and returns the sum."""
    quarters = int(input("How many quarters do you want to give: "))
    dime = int(input("How many dime do you want to give: "))
    nickel = int(input("How many nickel do you want to give: "))
    penny = int(input("How many penny do you want to give: "))

    result =  (quarters*0.25) + (dime*0.10) + (nickel*0.05) + (penny*0.01)
    return float("{:.2f}".format(result))


def check_money(input, MENU, money):
    """Checks if the money is sufficient or not. Returns True if money is sufficient."""
    cost = MENU[input]['cost']

    if cost <= money:
        return True

    return f"Sorry! Your money is insufficient. Refund of {money} given."


def resources_and_profit(input, MENU, resources):
    """It reduces the resources after every successful order and increments the profit."""
    global profit

    profit += MENU[input]['cost']
    resources['water'] -= MENU[input]['water']
    resources['coffee'] -= MENU[input]['coffee']
    resources['milk'] -= MENU[input]['milk']


def return_change(input, MENU, money):
    """Returns the change! Output is a string."""
    change =  money - MENU[input]['cost']
    return "Here is ${:.2f} in change.".format(change)


def give_report(resources, profit):
    """Gives report of the resources left in the Coffee Maker Machine."""
    print(f"Water: {resources['water']} mL.")
    print(f"Coffee: {resources['coffee']} g.")
    print(f"Milk: {resources['milk']} mL.")
    print(f"Money: ${profit}.") 

        

# This is our Menu (Espresso, Latte, Cappuccino)
# Capital letter for MENU as we don't change it anywhere further in the code
MENU = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "cost": 1.5,
        "milk": 0,
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5,
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0,
    }
}


# These are the resources available in the Coffee Maker Machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


profit = 0


# Just print all the details so the customer can make the right choice
MENU_LOGO = """
We have three hot coffee options available:

Espresso        $ 1.50
Latte           $ 2.50
Cappuccino      $ 3.00

"""


print("""
Here's a guide for the maintainers of the Coffee Maker Machine.
When asked 'What would you like to choose?'
1. 'off' as an input would turn off the machine.
2. 'report' as an input would output the remaining resources left in the machine.
""")


while True:
    print(MENU_LOGO)
    user_input = input("What would you like to choose? ").lower()

    if user_input == 'report':
        give_report(resources, profit)

    elif user_input == 'off':
        break
    
    elif user_input != 'espresso' and user_input != 'cappuccino' and user_input != 'latte':
        print("You gave an invalid command to the Coffee Maker Machine. Please try again!")
        continue 

    else:
        if check_requirements(user_input, MENU, resources) == True:
            money_input = user_money()

            if check_money(user_input, MENU, money_input) == True:
                resources_and_profit(user_input, MENU, resources)
                print(return_change(user_input, MENU, money_input))
                print(f"Here's your {user_input}. Enjoy!")

            else:
                print(check_money(user_input, MENU, money_input))
        
        else:
            print(check_requirements(user_input, MENU, resources))
