import sys

sys.path.append('../')
from util import macro

def start():
  p0()
  # p1()
  # p2()

def p0():
  macro.moduleStart("")
  height = float(input("enter your height in m: \n"))
  weight = float(input("enter your weight in kg: \n"))
  print(f"Your BMI is: {int(weight / height**2)}")

def p1():
  macro.moduleStart("hmm...s")

def p2():
  macro.moduleStart("")

start()