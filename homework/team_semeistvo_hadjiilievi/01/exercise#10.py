names = input().split()
n = int(input())

index_to_remove = (n - 1) % len(names)
while len(names) != 1:
    name = names.pop(index_to_remove)
    print(f'Removed {name}')
    index_to_remove = (index_to_remove + n - 1) % len(names)

print(f'Last is {names[0]}')