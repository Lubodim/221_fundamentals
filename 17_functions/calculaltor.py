# def add(a, b):
#     result = a + b
#     return result
# def subtract(a, b):
#     result = a - b
#     return result
# def multiply(a, b):
#     result = a * b
#     return result
# def divide(a, b):
#     if b == 0:
#         return "you can not divide by 0"
#     result = a / b
#     return result
# def input_func():
#     number1 = float(input("Enter the first number: "))
#     number2 = float(input("Enter the second number: "))
#     operator = input("Choice between + - * / or Stop for END: ")
#     return number1, number2, operator
# def print_func():
#     print(main_func(input_func))
# def main_func(input_f):
#     while True:
#         num1, num2, oper = input_f()
#         if oper.lower() == "stop":
#             return
#         elif oper == "+":
#             result = add(num1, num2)
#         elif oper == "-":
#             result = subtract(num1, num2)
#         elif oper == "*":
#             result = multiply(num1, num2)
#         elif oper == "/":
#             result = divide(num1, num2)
#         else:
#             print("Invalid operator")
#             continue
#         return result
# print_func()

