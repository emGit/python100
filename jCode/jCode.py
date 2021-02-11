from util import constants

def start():
  print()
  # p0()
  # p1()
  # p2()

def p0():
  print(constants.space)
  #1. Create a greeting for your program.
  name = input("What's your name? \n")

  print(f'\nHello, {name}!')

  #2. Ask the user for the city that they grew up in.
  city = input(f'\nSo, {name}, where did you grow up? \n').lower()

  #3. Ask the user for the name of a pet.

  pets = input('\nDo you have any pets? \n')

  if (pets == "yes" or pets == "Yes"):
    pet_name = input("\nWhat is your pet's name?\n")
  else:
    print("\nAh, I see.")
    animal_array = ["Cosmo", "Fluff", "Korra", "Wiggles", "Roach"]
    import random

    pet_name = random.choice(animal_array)

  #4. Combine the name of their city and pet and show them their band name.

  print(f'\nI think {pet_name}{city} would make a sick band name for you.')

  #5. Make sure the input cursor shows on a new line, see the example at:
  #   https://band-name-generator-end.appbrewery.repl.run/

  #input(prompting text), len(variable), variable.lower()

def p1():
  print(constants.space)

def p2():
  print(constants.space)