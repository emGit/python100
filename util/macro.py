from util import constants
import os

def cls():
  os.system('cls' if os.name=='nt' else 'clear')
# Clear the screen
# cls()

def moduleStart(title):
  print(constants.space)
  print(title)