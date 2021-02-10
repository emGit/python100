import sys

sys.path.append('../')
from util import macro

def start():
  # p0()
  p1()
  # p2()

def p0():
  macro.moduleStart("Scope")
  enemies = 1
  def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

  increase_enemies()
  print(f"enemies outside function: {enemies}")

  # Local Scope
  def drink_potion():
    potion_strength = 2
    print(potion_strength)

  drink_potion()
  print(potion_strength)

  # Global Scope
  player_health = 10

  def game():
    def drink_potion():
      potion_strength = 2
      print(player_health)
    drink_potion()
  print(player_health)

  # There is no Block Scope
  game_level = 3

  # noinspection PyUnboundLocalVariable
  def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
      new_enemy = enemies[0]
    print(new_enemy)

  # Modifying Global Scope
  enemies = 1

  def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

  enemies = increase_enemies()
  print(f"enemies outside function: {enemies}")

  #Global Constants
  PI = 3.14159
  URL = "https://www.google.com"
  TWITTER_HANDLE = "@yu_angela"

def p1():
  macro.moduleStart("Guess")
  import random
  print("Welcome to the number guessing game.")
  mode = input("Type 'easy' or 'hard'.\n")
  if mode == 'hard': lives = 5
  else: lives = 10
  target = random.randint(1, 100)
  while lives > 0:
    print(f"You have {lives} attempts remaining.")
    guess = int(input("Make a guess: "))
    if guess == target:
      print("Correct! You win.")
      input("Press Enter to continue...\n")
      p1()
    if guess > target: print("Too high.")
    if guess < target: print("Too low.")
    lives -= 1
  print("You lose! No attempts remain.")
  input("Press Enter to continue...\n")
  p1()

def p2():
  macro.moduleStart("")

start()