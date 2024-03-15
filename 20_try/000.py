def divide(a, b):
    return int(a) / int(b)


while True:
    num1 = input()
    num2 = input()
    try:
        print(divide(num1, num2))
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except ValueError:
        print("You cannot divide by characters")
    else:
        print("My program works correctly")
    finally:
        print("That is my program")
