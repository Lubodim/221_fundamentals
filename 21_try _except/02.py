class Spiridon(Exception):
    pass


def sum_list(lst):
    if len(lst) == 1 and type(lst[0]) == str:
        raise Spiridon
    if not lst:
        raise IndexError
    result = 0
    for i in lst:
        result += int(i)
    return result
my_list = input().split()

try:
    print(sum_list(my_list))
except ValueError:
    print("You can not sum int and str!")
except IndexError:
    print("You can not sum empty list!")
except Spiridon:
    print("U must split element by spaces")
