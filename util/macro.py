from os import name, system
from time import sleep

from util import constants

def cls():
  os.system('cls' if os.name=='nt' else 'clear')
# Clear the screen
# cls()

# define our clear function
def clear():
  sleep(2)
  # for windows
  if name=='nt': _ = system('cls')
  # for mac and linux(here, os.name is 'posix')
  else: _ = system('clear')

def moduleStart(title):
  print(constants.space)
  print(title)