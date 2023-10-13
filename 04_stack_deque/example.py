my_stack = [1, 2, 3, 4, 5, 6]

a = my_stack.pop()
print(a)
a = a ** 2
my_stack.append(a)
b = my_stack.remove(3)
print(b)
print(my_stack)
