from random import sample

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
player_1_name = input("Enter a name of first player: ")
player_2_name = input("Enter a name of second player: ")

player_1_num = "".join(str(x) for x in sample(numbers, 4))
player_2_num = "".join(str(x) for x in sample(numbers, 4))

print(player_1_num)
print(player_2_num)
help_list = []
while True:
    gues = input(f"{player_1_name.upper()} must enter a gues number: ")
    print()
    if gues == player_2_num:
        print(f"Result for {player_1_name.upper()} gueses: ")
        print(("Бик \n" * 4))
        print(f"{player_1_name.upper()} is winner")
        exit()
    print(f"Result for {player_1_name.upper()} gueses: ")
    for i, ch in enumerate(player_2_num):
        for j, c in enumerate(gues):
            if c == ch and i == j:
                help_list.append("Бик")
            elif c == ch:
                help_list.append("Крава")
        if "Крава" in help_list and "Бик" in help_list:
            print("Бик")

        else:
            if help_list:
                print(*help_list, sep="\n")
        help_list.clear()
    print()

    player_1_name, player_2_name = player_2_name, player_1_name
    player_1_num, player_2_num = player_2_num, player_1_num