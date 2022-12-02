MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item]>=resources[item]:
            print(f"sorry there is not enough{item}")
            return False

    return True

def process_coins():
    print("Please insert coins")
    total = int(input("How many quarters? : "))*0.25
    total+=int(input("How many dimes? : "))*0.1
    total+=int(input("How many nickles? : ")) * 0.05
    total+=int(input("How many pennies : ")) * 0.01
    return total


def is_transaction_succesful(money_received,drink_cost):
    if money_received>=drink_cost:
        global profit
        profit+=drink_cost
        change=round(money_received-drink_cost,2)
        print(f"here is your change {change}")
        return True
    else:
        print("sorry that is not enough money.money refunded")
        return False


def make_coffee(drink_name,order_ingredient):
    for item in order_ingredient:
        resources[item]-=order_ingredient[item]
    print(f"Here is your drink {drink_name}")



def coffee_machine():
    logo=""" ____  ____  _____ _____ _____ _____   _      ____  ____  _     _  _      _____
/   _\/  _ \/    //    //  __//  __/  / \__/|/  _ \/   _\/ \ /|/ \/ \  /|/  __/
|  /  | / \||  __\|  __\|  \  |  \    | |\/||| / \||  /  | |_||| || |\ |||  \  
|  \__| \_/|| |   | |   |  /_ |  /_   | |  ||| |-|||  \_ | | ||| || | \|||  /_ 
\____/\____/\_/   \_/   \____\\____\  \_/  \|\_/ \|\____/\_/ \|\_/\_/  \|\____\
                                                                               """
    print(logo)
    is_on = True
    choice = input(f"What would you like? : ")
    if choice == "off":
        is_on = False

    elif choice == "Report":
        print(f"water: {resources['water']} ml,")
        print(f"milk : {resources['milk']} ml,")
        print(f"coffee: {resources['coffee']} g" ,)
        print(f"Money : ${profit}")

    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
        if is_transaction_succesful(payment,drink["cost"]):
            make_coffee(choice,drink["ingredients"])


coffee_machine()