initial_bites = int(input())
queue = []

while True:
    command = input()

    if command.lower() == "start":
        break
    else:
        queue.append(command)

while True:
    command = input()

    if command.lower() == "end":
        break

    if command.startswith("refill"):
        _, beets = command.split()
        beets = int(beets)
        initial_bites += beets
    else:
        person_name = queue.pop(0)
        bites = int(command)
        if initial_bites >= bites:
            print(f"{person_name} takes {bites} bites")
            initial_bites -= bites
        else:
            print(f"{person_name} must wait")

print(f"{initial_bites} bites left")
