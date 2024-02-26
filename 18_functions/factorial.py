# from collections import deque
# from datetime import datetime
#
# my_list = []
# my_que = deque()
#
# for i in range(1, 5_000_000):
#     my_list.append(i)
#     my_que.append(i)
#
# start = datetime.now()
# for _ in range(10_000):
#     my_list.pop(0)
# end = datetime.now()
# print(end - start)
#
#
# start1 = datetime.now()
# for _ in range(10_000):
#     my_que.popleft()
# end1 = datetime.now()
# print(end1 - start1)


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number to find its Factorial: "))

print(f"Factorial of {number} is {factorial(number)}")
