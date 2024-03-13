def neshto(num):
    if 2 <= num < 3:
        return 'Fail'
    elif 3 <= num < 3.50:
        return 'Poor'
    elif 3.50 <= num < 4.50:
        return 'Good'
    elif 4.50 <= num < 5.50:
        return 'Very Good'
    elif 5.50 <= num <= 6:
        return 'Excellent'
drugo = float(input())
print(neshto(drugo))
print(neshto(4))
