# -=-
# klas: 22115
# grupa: linux
# predal: 22115
# -=-

# zad. 9:
names = []

while True:
    command = input()

    if command == "END":
        print(f"{len(names)} people remaining.")
        break
    elif command == "PAID":
        while names:
            print(names.pop(0))
    else:
        names.append(command)
#
# # zad 10:
# initial_bites = int(input())
# queue = []
#
# while True:
#     command = input()
#
#     if command.lower() == "start":
#         break
#     else:
#         queue.append(command)
#
# while True:
#     command = input()
#
#     if command.lower() == "end":
#         break
#
#     if command.startswith("refill"):
#         _, beets = command.split()
#         beets = int(beets)
#         initial_bites += beets
#     else:
#         person_name = queue.pop(0)
#         bites = int(command)
#         if initial_bites >= bites:
#             print(f"{person_name} takes {bites} bites")
#             initial_bites -= bites
#         else:
#             print(f"{person_name} must wait")
#
# print(f"{initial_bites} bites left")
#
# # zad 11:
# children = input().split()
# n = int(input())
#
# index = 0
#
# while len(children) > 1:
#     index = (index + n - 1) % len(children)
#     removed_child = children.pop(index)
#
#     print(f"Removed {removed_child}")
#
# winner = children[0]
#
# print(f"Last is {winner}")