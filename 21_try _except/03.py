def float_to_integer(n):
    return int(n)
try:
    number = float(input())
except ValueError:
    print("You can not make string to integer")
try:
    print(float_to_integer(number))
except NameError:
    print("You must input a number")