import sys

sys.path.append('../')
from util import macro
from art import logo
from data import data
import random

macro.moduleStart("HigherLower")

new_data = []
a, b, c = None, None, None

def select():
    x = random.choice(new_data)
    new_data.remove(x)
    return x

def swap():
    global a, b, c
    print("Correct!")
    new_data.append(a)
    a = b
    b = c
    c = select()

def start():
    global a, b, c, new_data
    new_data = data
    a = select()
    b = select()
    c = select()
    print(print(logo))
    correct = True
    while correct:
        if input(f"Does {b.get('name')} have more followers than {a.get('name')}? ") == 'yes' or 'y':
            if b.get('follower_count') > a.get('follower_count'): swap()
            else: correct = False
        else:
            if last.get('follower_count') > first.get('follower_count'): correct = False
            else: swap()

    if input("You lose! Would you like to play again? ") == 'yes' or 'y': start()

start()