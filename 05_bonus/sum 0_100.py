total_sum = 0
total_even_sum = 0
total_odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        total_even_sum += i
    elif i % 2 == 1:
        total_odd_sum += i
    total_sum += i

print(total_sum)
print(total_even_sum)
print(total_odd_sum)