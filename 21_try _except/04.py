def dict_work(data_in):
    res = {}
    for i in range(0, len(data_in), 2):
        res[data_in[i]] = int(data_in[i + 1])
    return res


def check_names(data_in, names_in):
    try:
        for name in names_in:
            ages.append(data_in[name])
    except KeyError:
        print("This person does not exist in this dictionary")
        exit(0)


data = input().split()
names = input().split(", ")
ages = []

new_data = dict_work(data)
check_names(new_data, names)
print(*ages, sep=", ")
print("That was the ages of the persons")
