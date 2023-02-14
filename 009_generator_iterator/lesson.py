def squares(start, stop):
    for i in range(start, stop):
        yield i ** 2


x = squares(1, 11)

print(next(x))

for i in x:
    print(i)

print(next(x))
