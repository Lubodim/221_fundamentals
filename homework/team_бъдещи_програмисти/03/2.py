n = int(input("Enter the number of cars: "))
parked_cars = set()
for _ in range(n):
    action = input("Enter the car number in the format {IN}/{OUT}, {AAXXXXAA}: ")
    direction, car_number = action.split(", ")
    if direction == "IN":
        parked_cars.add(car_number)
    elif direction == "OUT":
        parked_cars.discard(car_number)
if parked_cars:
    for car_number in sorted(parked_cars):
        print(car_number)
else:
    print("Parking is empty!")
