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
