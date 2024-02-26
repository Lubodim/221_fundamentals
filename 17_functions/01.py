def neshto(a, b):
    power = a ** b
    return power

number, exponent = [int(x) for x in input().split(', ')]
# number, exponent = map(int, input().split(', '))

print(f" {number} to the power {exponent} is {neshto(number, exponent)}")
