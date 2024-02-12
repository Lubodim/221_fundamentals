data = input().split()
orders = input().split()
bar = {}
for i in range(0, len(data), 2):
    if data[i] not in bar:
        bar[data[i]] = 0
    bar[data[i]] = int(data[i + 1])

for o in orders:
    if o in bar.keys():
        print(f"We have {bar[o]} of {o} left")
    else:
        print(f"Sorry, we don't have {o}")