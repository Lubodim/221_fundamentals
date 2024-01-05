player_1_name = input()
player_2_name = input()

player_1_num = "1234"
player_2_num = "4321"
player_1_count = 0
player_2_count = 0
gues_1 = input()
gues_2 = input()
while True:
    if gues_1 == player_2_num:
        print(f"{player_1_name} is winner")
        break
    if gues_2 == player_1_num:
        print(f"{player_2_name} is winner")
        break
    for ch, i in enumerate(player_1_num):
        for c, j in enumerate(player_2_num):
            if c == ch and i == j:
                print("Бик")
                continue
            elif c == ch:
                print("Крава")

    gues_1 = input()
    gues_2 = input()

