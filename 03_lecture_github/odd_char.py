# print(ord("퟿"))
#
# print(chr(97))
for ch in range(55295 + 1):
    if ch % 50 == 0:
        print()
    print(chr(ch), end=', ')