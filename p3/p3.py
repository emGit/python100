from util import constants, macro

def start():
  p0()
  p1()
  p2()

def p0():
  macro.moduleStart("BMI Calculator")
  height = float(input("enter your height in m: \n"))
  weight = float(input("enter your weight in kg: \n"))
  print(f"Your BMI is: {int(weight/height**2)}")

def p1():
  print(constants.space)

def p2():
  print(constants.space)