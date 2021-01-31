from util import constants

def start():
  p0()
  p1()
  p2()

def p0():
  print(constants.space)
  print(
    "Day 1 - Python Print Function!\n"
    "The function is declared like this:\n"
    "print('what to print')")
  print(constants.space)
  print('Day 1 - String Manipulation\n'
        'String Concatenation is done with the \"+\" sign.\n'
        'e.g. print("Hello " + "world")\n'
        'New lines can be created with a backslash and n.')
  print(constants.space)
  length = len(input("What is your name? "))
  print(length)

def p1():
  print(constants.space)
  a = input("a:")
  b = input("b:")
  c = a
  #Swap a and b;
  a = b
  b = c
  print("a = "+a)
  print("b = "+b)

def p2():
  print(constants.space)
  print("Welcome to the band name generator.")
  city = input("Which city did you grow up in?\n")
  print(city)
  pet = input("What is the name of a pet?\n")
  print("Your band name could be "+city+" "+pet)