row_col = int(input())
total_sum = 0
for row in range(row_col):
    # num = [int(x)for x in input().split(", ")]
    num = list(map(int, input().split(", ")))
    print(num)
    total_sum += sum(num)
print(total_sum)

# print(sum(sum(int(x)for x in input().split(", ")) for _ in range(int(input()))))

