# def sorting(value):
#     return value[1]

# def squares(number):
    # return number ** 2

x = [[1, 5], [3, 6], [7, 2], [2, 1]]
print(x)
x.sort(key=lambda value: value[1])
print(x)

sum_numer = lambda a, b: a + b
print(sum_numer(2, 5))