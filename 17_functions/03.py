koki = map(float, input().split(' '))
result = lambda x: [abs(x) for x in koki]
print(result(koki))
