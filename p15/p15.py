MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}

resources = {"water":300, "milk":200, "coffee":100, "money":0}

def hasResources(choice):
    for item in MENU[choice]["ingredients"]:
        if resources[item] >= MENU[choice]["ingredients"][item] is False:
            print("Sorry not enough resources available!")
            return False
    return True

def processCoins(choice, cost):
    inserted = sum([
        int(input("How many pennies? ")) * .01,
        int(input("How many nickels? ")) * .05,
        int(input("How many dimes? ")) * .1,
        int(input("How many quarters? ")) * .25])
    if inserted >= cost:
        change = round(inserted - cost, 2)
        if change > 0: print(f"Here is your change: ${change}")
        resources["money"] += cost
        for item in MENU[choice]["ingredients"]: resources[item] -= MENU[choice]["ingredients"][item]
        print(f"Here is your {choice}. Enjoy!")
    else: print("Sorry that is not enough money. Money refunded.")

choice = input("What would you like? (espresso/latte/cappuccino): ")
while choice != 'off':
    if choice == "report": print(resources)
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if hasResources(choice): processCoins(choice, MENU[choice]["cost"])
    else: print("Invalid choice. Try Again")
    choice = input("What would you like? (espresso/latte/cappuccino): ")