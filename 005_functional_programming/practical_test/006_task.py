# Написать программу, которая для произвольного списка находит число / числа, наиболее часто встречающееся
# в данном списке и возвращающее их также в виде списка.
#         Примеры:
#         [1, 2, 3, 4, 7, 9, 9] → [9]
#         [1, 2, 4, 6, 4, 6] → [4,6]


random_list = [1, 2, 3, 4, 7, 9, 9]

test_lst = [1, 2, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7,]
# counter = {}
#
# for num in test_lst:
#     counter[num] = test_lst.count(num)
# print(counter)
#
# result = []
# for x in counter.keys():
#     if counter[x] == max(counter.values()):
#         result.append(x)
# print(result)

max_count = 0
result = []
for num in test_lst:
    if test_lst.count(num) > max_count:
        max_count = test_lst.count(num)

for num in test_lst:
    if test_lst.count(num) == max_count and num not in result:
        result.append(num)

print(result)
