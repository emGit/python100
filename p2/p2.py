from util import constants, macro

def start():
    # p0()
    # p1()
    # p2()
    # p3()
    # p4()
    p5()

def p0():
    print(constants.space)
    print("Hello"[0])
    print("123" + "456")
    print(123 + 456)
    print(123.56 + 23.22)
    print(True)
    a = float(123)
    print(type(a))
    print(70 + float(100.5))
    print(str(70) + str(100))

def p1():
    print(constants.space)
    twoDigitNumber = input("Type a two digit number.\n")
    first = twoDigitNumber[0]
    second = twoDigitNumber[1]
    print(twoDigitNumber)
    print(int(first) + int(second))

def p2():
    macro.moduleStart("BMI calculator")
    height = float(input("enter your height in m: \n"))
    weight = float(input("enter your weight in kg: \n"))
    bmi = weight / height ** 2
    bmiAsInt = int(bmi)
    print(bmiAsInt)

def p3():
    print(constants.space)
    print(round(8 / 3, 2))
    print(8 // 2)
    result = 4 / 2
    result /= 2
    print(result)
    score = 0
    score += 1
    print(score)
    height = 1.8
    isWinning = True
    print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

def p4():
    print(constants.space)
    age = int(input("What is your current age in years? \n"))
    death = 90
    yearsRemaining = death - age

    days = yearsRemaining * 365
    weeks = yearsRemaining * 52
    months = yearsRemaining * 12

    print(f"You have {days} days, {weeks} weeks,{months} months,")

def p5():
    print(constants.space)
    print(f"Welcome to the tip calculator.")
    bill = float(input("What was the total bill? $"))
    tipPercent = float(input("What percentage tip would you like to give?"
                             " 10, 12, or 15? "))
    people = int(input("How many people to split the bill? "))
    fCost = "{:.2f}".format(bill * (1 + tipPercent / 100) / people)
    # print(f"Each person should pay: ${round(cost, 2)}")
    print(f"Each person should pay: ${fCost}")