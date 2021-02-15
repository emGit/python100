import sys

sys.path.append('../')
from util import macro

def start():
    # p0()
    # p1()
    p2()

def p0():
    macro.moduleStart("Function Outputs")

    def format_name(f_name, l_name):
        return f_name.title() + " " + l_name.title()

    print(format_name(input("what is your name ? \n"), input("what is your last name ? \n")))

def p1():
    macro.moduleStart("Leap")

    def is_leap(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0: return True
                else: return False
            else: return True
        else: return False

    def days_in_month(year, month):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap(year) and month == 2: return 29
        return month_days[month - 1]

    # 🚨 Do NOT change any of the code below
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(days)

def p2():
    macro.moduleStart("Calculator")
    from art import logo
    from util.macro import cls
    def add(n1, n2): return n1 + n2
    def subtract(n1, n2): return n1 - n2
    def multiply(n1, n2): return n1 * n2
    def divide(n1, n2): return n1 / n2

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    def calculator():
        print(logo)
        num1 = float(input("What's the first number?: "))
        for symbol in operations: print(symbol)
        should_continue = True
        while should_continue:
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What's the next number?: "))
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            if input(f"Type 'y' to continue calculating with {answer},"
                     f" or type 'n' to start a new calculation: ") == 'y':
                num1 = answer
            else:
                should_continue = False
                # print(space)
                cls()
                calculator()
    calculator()

start()