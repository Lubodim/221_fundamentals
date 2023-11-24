cars = []
parked_cars = []

n = int(input())

for i in range(n):
    user_inputs = input()
    cars.append(user_inputs)

for user_input in cars:
    user_input_split = user_input.split(", ")
    if len(user_input_split) == 2:
        command = user_input_split[0]
        car = user_input_split[1]
        if command == "IN":
            parked_cars.append(car)
        elif command == "OUT":
            if car in parked_cars:
                parked_cars.remove(car)

if len(parked_cars) == 0:
    print("Parking lot is empty.")
else:
    for i in parked_cars:
        print(i)