# 1, 2, 3, 4, 5, 6, 7, 8, 9
# print(*input().split(', ')[::-1])

#5
# text = [int(t) for t in input().split(', ')]
# print(' '.join(str(t) for t in text[::-1]))



#4
txt = input().split(', ')
text = [int(t) for t in txt[::-1] if int(t) % 2 == 1]
print(*text)

#3
# my_list = input().split(', ')
# text = list(map(int, my_list))
# print(*text[::-1])


#2
# text = input().split(", ")
# for _ in range(len(text)):
#     print(text.pop(), end=" ")


#1
# text = input().split(", ")
# len_test = len(text)
# for _ in range(len_test):
#     print(text.pop(), end=" ")