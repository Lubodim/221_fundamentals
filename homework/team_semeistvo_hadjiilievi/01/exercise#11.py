bites = int(input())

names = []

inputs = []

while True:
    user_input = input()
    if user_input == "Start":
        break
    else:
        names.append(user_input)

while True:
    user_input = input()
    if user_input == "End":
        break
    else:
        inputs.append(user_input)


for list_input in inputs:
    if "refill" in list_input:
        split_input = list_input.split()
        bites = bites + int(split_input[1])
    elif list_input == "End":
        break
    else:
        if bites >= int(list_input):
            bites = bites - int(list_input)
            name = names.pop(0)
            print(f'{name} take bites')
        else:
            name = names.pop(0)
            print(f'{name} must wait')

print(f'{bites} bites left')
