from random import choice
from collections import deque
from time import sleep
fighters = deque([
    "Scorpion", "Liu Kang", "Sub Zero", "Kano",
    "Sonya Blade", "Raiden", "Baraka", "Jax",
    "Johnny Cage", "Kung Lao", "Jade",
    "Noob Saibot", "Kabal", "Geras", "D'Vorah",
    "Jacqui Briggs", "Scarlett", "Cassie Cage",
    "Kotal Kahn", "Erron Black"
])
killed = []
print("This is a Mortal Combat Game!")
print()

player_name = input("Enter your name here: ")
player_blood = 100
player_shield = 80
player_power = 70
is_continuous = False

while True:
    if fighters:
        comp_name = fighters.popleft()
    else:
        print(f"{player_name} WIN THE GAME\nHe/She killed {','.join(killed)}")
        break
    comp_blood = 100
    comp_shield = choice(range(20, 80))
    comp_power = choice(range(20, 70))
    player_blood = 100

    if is_continuous:
        while True:
            question = input("Do you want to continue fight? Y/N: ").upper()
            if question == "Y":
                break
            elif question == "N":
                print(f"{player_name} loose, but he/she kills {', '.join(killed)}")
                print("GAME OVER!")
                exit()
            else:
                print("Incorrect answer")
                print()
                continue
        player_power += 3
        player_shield += 3
    if len(killed) % 3 == 0:
        player_blood += (10 * (len(killed)//3))
        player_power -= 4
        player_shield -= 4
        comp_blood += (10 * (len(killed)//4))
        comp_shield -= 4
        comp_power -= 4
    is_continuous = True
    print("Loading...", end="")
    sleep(2)
    for _ in range(5):
        print(".", end="")
        sleep(1)
    print()
    while True:
        print(f"{player_name} will hit {comp_name}")
        print(f"Before hit {comp_name} have {comp_blood} blood")
        print()
        sleep(2)
        if player_power >= comp_shield:
            comp_blood -= (player_power - comp_shield)
        else:
            comp_blood -= player_power//6
        print(f"After hit {comp_name} have {comp_blood} blood")
        print()
        sleep(1)
        if comp_blood <= 0:
            print(f"{player_name} killed, {comp_name}")
            killed.append(comp_name)
            break

        print(f"{comp_name} will hit {player_name}")
        print(f"Before hit {player_name} have {player_blood} blood")
        print()
        sleep(1)
        if comp_power >= player_shield:
            player_blood -= (comp_power - player_shield)
        else:
            player_blood -= comp_power//6
        print(f"After hit {player_name} have {player_blood} blood")
        print()
        sleep(1)
        if player_blood <= 0:
            print(f"{player_name} loose, but he/she kills {', '.join(killed)}")
            print("GAME OVER!")
            exit()

