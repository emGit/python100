import sys

sys.path.append('../')
from util import macro

class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {"water": water,
                            "milk": milk,
                            "coffee": coffee}

class Menu:
    CURRENCY = "$"

    def __init__(self):
        self.profit = 0
        self.money_received = 0
        self.menu = [MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
                     MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)]

    def report(self): print(f"Money: {self.CURRENCY}{self.profit}")

    def get_items(self):
        options = ""
        for item in self.menu: options += f"{item.name}/"
        return options

menu = Menu()

def start():
    p0()
    # p1()
    # p2()

def p0():
    macro.moduleStart("")
    height = float(input("enter your height in m: \n"))
    weight = float(input("enter your weight in kg: \n"))
    print(f"Your BMI is: {int(weight / height ** 2)}")

def p1():
    macro.moduleStart("")

def p2():
    macro.moduleStart("")

start()