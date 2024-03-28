def divide(a, b):
    return float(a) / float(b)


try:
    num1, num2 = input().split(", ")
except ValueError:
    print("You must have exactly two numbers")

try:
    print(divide(num1, num2))
except ZeroDivisionError:
    print("You can not divide by ZERO")
except ValueError:
    print("You can not divide by symbol")
except NameError:
    print("You must input second number")
