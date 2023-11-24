n, m = tuple(map(int, input().split()))

# numbers = input().split()
# n = int(numbers[0])
# m = int(numbers[1])

set_n = set()
set_m = set()

for _ in range(n):
    numb = int(input())
    set_n.add(numb)
for _ in range(m):
    set_m.add(int(input()))

print(set_n)
print(set_m)
print()
print(set_n.intersection(set_m))