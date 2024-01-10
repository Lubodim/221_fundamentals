from random import sample

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
player_1_name = input("Enter a name of first player: ")
player_2_name = input("Enter a name of second player: ")

player_1_num = "".join(str(x) for x in sample(numbers, 4))
player_2_num = "".join(str(x) for x in sample(numbers, 4))

print(player_1_num)
print(player_2_num)
while True:

    gues = input(f"{player_1_name.upper()} must enter a gues number: ")

    if gues == player_2_num:
        print(f"Result for {player_1_name.upper()} gueses: ")
        print(("Бик \n" * 4))
        print(f"{player_1_name.upper()} is winner")
        exit()
    print(f"Result for {player_1_name.upper()} gueses: ")
    for i, ch in enumerate(player_2_num):
        for j, c in enumerate(gues):
            if c == ch and i == j:
                print("Бик")
            elif c == ch:
                print("Крава")

    print()

    player_1_name, player_2_name = player_2_name, player_1_name
    player_1_num, player_2_num = player_2_num, player_1_num

# ml = ["a", "b", "c", "d", "e", "f"]
# for j, c in enumerate(ml):
#     print(f"index - {j} element {c}")