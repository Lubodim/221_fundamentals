
num1, num2, op = [int(i) if i.isdigit() else str(i) for i in input().split()]

if op == "+":
    result = lambda x, y: x + y
elif op == "-":
    result = lambda x, y: x - y
elif op == "*":
    result = lambda x, y: x * y
elif op == "/":
    result = lambda x, y: x / y if y != 0 else "You can`t divide by ZERO"

print(result(num1, num2))
