from util import macro

def start():
  # p0()
  # p1()
  # p2()
  # p3()
  # p4()
  # p5()
  p6()
def p0():
  macro.moduleStart("Odd Even")
  number = int(input("Which number do you want to check? "))
  if number % 2 == 0: print(f"Number: {number} is even.")
  else: print(f"Number: {number} is odd.")

def p1():
  macro.moduleStart("BMI")
  height = float(input("enter your height in m: "))
  weight = float(input("enter your weight in kg: "))
  bmi = round(weight / height**2)
  if bmi < 18.5: print(f"Your BMI is {bmi}, you are underweight.")
  elif bmi < 25: print(f"Your BMI is {bmi}, you have a normal weight.")
  elif bmi < 30: print(f"Your BMI is {bmi}, you overweight.")
  elif bmi < 35: print(f"Your BMI is {bmi}, you are obese.")
  else: print(f"Your BMI is {bmi}, you are clinically obese.")

def p2():
  macro.moduleStart("Leap Year")
  year = int(input("Which year do you want to check? "))
  if year % 4 == 0 & year % 100 != 0: print("Leap")
  elif year % 4 == 0 & year % 100 == 0 & year % 400 == 0: print("Leap")
  else: print("Not Leap")

def p3():
  macro.moduleStart("Rollercoaster")
  print("Welcome to the rollercoaster!")
  height = int(input("What is your height in cm? "))
  bill = 0
  if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
      bill = 5
      print("Child tickets are $5.")
    elif age <= 18:
      bill = 7
      print("Youth tickets are $7.")
    elif 45 <= age <= 55: print("Everything is going to be ok. Have a free ride on us!")
    else:
      bill = 12
      print("Adult tickets are $12.")
    wantsPhoto = input("Do you want a photo taken? Y or N. ")
    if wantsPhoto == "Y": bill += 3
    print(f"Your final bill is ${bill}")
  else: print("Sorry, you have to grow taller before you can ride.")

def p4():
  macro.moduleStart("Pizza")
  print("Welcome to Python Pizza Deliveries!")
  size = input("What size pizza do you want? S, M, or L ")
  addPepperoni = input("Do you want pepperoni? Y or N ")
  extraCheese = input("Do you want extra cheese? Y or N ")

  bill = 0
  if size == "S": bill += 15
  elif size == "M": bill += 20
  else: bill += 25

  if addPepperoni == "Y":
    if size == "S": bill += 2
    else: bill += 3

  if extraCheese == "Y": bill += 1
  print(f"Your bill is: ${bill}")

def p5():
  macro.moduleStart("Love")
  print("Welcome to the Love Calculator!")
  name1 = input("What is your name? \n")
  name2 = input("What is their name? \n")
  combined = (name1 + name2).lower()
  t = combined.count("t")
  r = combined.count("r")
  u = combined.count("u")
  e = combined.count("e")
  true = t + r + u + e
  l = combined.count("l")
  o = combined.count("o")
  v = combined.count("v")
  e = combined.count("e")
  love = l + o + v + e
  score = int(str(true) + str(love))
  if score < 10 or score > 90: print(f"Your score is {score}, you go together like coke and mentos.")
  elif score >= 40 or score <= 50: print(f"Your score is {score}, you are alright together.")
  else: print(f"Your score is {score}!")

def p6():
  macro.moduleStart("Treasure")
  print('''
  *******************************************************************************
            |                   |                  |                     |
   _________|________________.=""_;=.______________|_____________________|_______
  |                   |  ,-"_,=""     `"=.|                  |
  |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
   _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
  |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
  |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
   _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
  |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
  |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
  ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
  /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
  ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
  /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
  ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
  /______/______/______/______/______/______/______/______/______/______/_____ /
  *******************************************************************************
  ''')
  print("Welcome to Treasure Island.")
  print("Your mission is to find the treasure.")
  choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
  if choice1 == "left":
    choice2 = input(
      'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
      choice3 = input(
        "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
      if choice3 == "red": print("It's a room full of fire. Game Over.")
      elif choice3 == "yellow": print("You found the treasure! You Win!")
      elif choice3 == "blue": print("You enter a room of beasts. Game Over.")
      else: print("You chose a door that doesn't exist. Game Over.")
    else: print("You get attacked by an angry trout. Game Over.")
  else: print("You fell into a hole. Game Over.")