from copy import copy, deepcopy
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list_2 = deepcopy(my_list)

for d in my_list:
    my_list_2.pop()
    print(my_list)

