import itertools

# counter = itertools.count()
#
# # x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #
# # for i in x:
# #     print(next(counter), ':', i, sep='')
#
# data = [100, 200, 300, 400]
#
# # daily_data = zip(counter, data)
# # print(list(daily_data))
# #
# # print(list(enumerate(data, 100)))
#
# daily_data = itertools.zip_longest(data, range(10), fillvalue=False)
# print(list(daily_data))

# counter = itertools.count(start=-100.5, step=-0.5)

# counter = itertools.cycle(['event', 'odd'])
#
# for x in range(100):
#     print(x, next(counter))

# counter = itertools.repeat(2)
#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# resault = map(lambda x, y: x ** y, range(100), itertools.repeat(2))
# for x in resault:
#     print(x)

# resault = itertools.starmapmap(lambda x, y: x ** y, [(0 , 2), (1, 2), (3, 5)])
# for x in resault:
#     print(x)

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
selectors = [True, False, False, True]
names = ['Jack', 'Sarah']

# NO ORDER / NO REPEAT
# res = itertools.combinations(letters, 3)
# for x in res:
#     print(x)

# ORDERED / NO REPEAT
# res = itertools.permutations(letters, 3)
# for x in res:
#     print(x)

# ORDERED / REPEATING
# res = itertools.product(numbers, letters, repeat=2)
# for x in res:
#     print(x)

#NO ORDER / REPEATING
# res = itertools.combinations_with_replacement(numbers, 4)
# for x in res:
#     print(x)

# combined = itertools.chain(letters, numbers, 'hello')
# print(list(combined))

# combined = itertools.islice({1, 2, 3, 4, 5, 6, 7, 8}, 0, 5, 2)
# print(list(combined))

# res = itertools.compress(letters, numbers)
# def more_than_two(x):
#     return x > 2
#    ## return not  > 2
# res2 = filter(more_than_two, numbers2)
# print(list(res2))
#
# res3 = itertools.filterfalse(lambda x: x > 2, numbers2)
# print(list(res3))

# res = itertools.dropwhile(lambda x: x >2, numbers2)
# print(list(res))
#
# res2 = itertools.takewhile(lambda x: x > 2, numbers2)
# print(list(res2))

# res3 = itertools.accumulate(numbers2)
# print(list(res3))
