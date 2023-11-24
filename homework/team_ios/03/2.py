n = int(input())

parking_lot = []

for _ in range(n):
    entry_exit, car_number = input().split(', ')

    if entry_exit.lower() == "in":
        parking_lot.append(car_number)
    elif entry_exit.lower() == "out" and car_number in parking_lot:
        parking_lot.remove(car_number)

if parking_lot:
    print('\n'.join(parking_lot))
else:
    print("Паркинга е празен")