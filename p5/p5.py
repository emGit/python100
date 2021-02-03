from util import constants, macro

def start():
  # p0()
  # p1()
  # p2()
  # p3()
  # p4()
  p5()

def p0():
  macro.moduleStart("Fruits")
  fruits = ["Apple", "Peach", "Pear"]
  for i in fruits:
    print(i)
    print(i+" Pie")
  print(fruits)

# noinspection PyTypeChecker,PyUnboundLocalVariable
def p1():
  macro.moduleStart("Height")
  heights = input("Input a list of heights. e.g 160 170. ").split()
  for i in range(0, len(heights)): heights[i] = int(heights[i])
  sum = 0
  for i in heights: sum += i
  len = 0
  for _ in heights: len += 1
  print(f"Average height is {int(sum/len)}")

# noinspection PyTypeChecker,PyUnboundLocalVariable
def p2():
  macro.moduleStart("Scores")
  scores = input("Input a list of scores. e.g 99 82. ").split()
  highest = -1
  for i in range(0, len(scores)): scores[i] = int(scores[i])
  for i in scores:
    if i>highest: highest = i
  print(f"The highest score is {highest}")

def p3():
  macro.moduleStart("Range")
  total = 0
  for number in range(1, 101): total += number
  print(total)
  total = 0
  for number in range(2, 100, 2): total += number
  print(total)

def p4():
  macro.moduleStart("FizzBuzz")
  for number in range(1, 100):
    if number%3 and number%5==0: print("FizzBuzz")
    elif number%3==0: print("Fizz")
    elif number%5==0: print("Buzz")
    else: print(number)

def p5():
  macro.moduleStart("Password")
  import random
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  print("Welcome to the PyPassword Generator!")
  nr_letters = int(input("How many letters would you like in your password?\n"))
  nr_symbols = int(input(f"How many symbols would you like?\n"))
  nr_numbers = int(input(f"How many numbers would you like?\n"))

  #Easy
  # password = ""
  # for i in range(1, nr_letters+1): password += random.choice(letters)
  # for i in range(1, nr_symbols+1): password += random.choice(symbols)
  # for i in range(1, nr_numbers+1): password += random.choice(numbers)
  # print(password)

  #Hard Level
  password_list = []
  for char in range(1, nr_letters+1): password_list.append(random.choice(letters))
  for char in range(1, nr_symbols+1): password_list += random.choice(symbols)
  for char in range(1, nr_numbers+1): password_list += random.choice(numbers)
  print(password_list)

  random.shuffle(password_list)
  print(password_list)
  password = ""
  for char in password_list: password += char
  print(f"Your password is: {password}")

start()