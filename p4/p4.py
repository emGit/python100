import random

from util import macro

def start():
    # p0()
    # p1()
    # p2()
    p3()

def p0():
    macro.moduleStart("Coin Toss")
    if random.randint(0, 1) == 0: print("Tails")
    else: print("Heads")

def p1():
    macro.moduleStart("Food Payment")
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")
    from random import randint
    print(names[randint(0, len(names) - 1)])

def p2():
    macro.moduleStart("Treasure")
    row1 = ["⬜", "⬜", "⬜"]
    row2 = ["⬜", "⬜", "⬜"]
    row3 = ["⬜", "⬜", "⬜"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")
    map[int(position[0]) - 1][int(position[1]) - 1] = "X"
    print(f"{row1}\n{row2}\n{row3}")

def p3():
    macro.moduleStart("Rock-Paper-Scissors")
    import random

    rock = '''
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  '''

    paper = '''
      _______
  ---'   ____)____
            ______)
            _______)
           _______)
  ---.__________)
  '''

    scissors = '''
      _______
  ---'   ____)____
            ______)
         __________)
        (____)
  ---.__(___)
  '''
    game_images = [rock, paper, scissors]
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
        return
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2: print("You win!")
    elif computer_choice == 0 and user_choice == 2: print("You lose")
    elif computer_choice > user_choice: print("You lose")
    elif user_choice > computer_choice: print("You win!")
    elif computer_choice == user_choice: print("It's a draw")

start()