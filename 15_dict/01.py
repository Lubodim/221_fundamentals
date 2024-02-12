data = input().split()
class_221 = {}
for el in range(0, len(data), 2):
    name = data[el]
    number = data[el + 1]
    if name not in class_221.keys():
        class_221[name] = int(number)
print(class_221)