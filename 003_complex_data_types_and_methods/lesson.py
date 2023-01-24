# empty_lst = []
# empty_lst = list()
# print(type(empty_lst))

# world = 'world'
# filled_lst = [123, 0.12312, True, 'Hello world!', [1, [9, 'Hello world!', 9, 9], 3, 4]]
# print(len(filled_lst))
# print(filled_lst[-1][1][1].upper())

courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', 'art', '123']
nums = [1, 5, 6, 8, 3, 4, 2, 92.32]

# courses[1] = 'Art'
# print(courses)
# courses.append('Art')  # добавление одного значения в список
# print(courses)
# courses.extend(['Art', 'English'])  # добавление нескольких значений
# print(courses)
# courses.insert(0, 'English')  # добавление в список, на конкретное место
# print(courses)

# courses.remove('Math')  #удаляет первый найденные элимент
# print(courses)
# popped = courses.pop(0)  #удаляет последний элемент из списка, в скобках номер элемента, вместо последнего
# print(courses)
# print(popped)

# courses.reverse()  # разварачивает порядок элементов в списке
# print(courses)
# print(reversed(courses))

# courses.sort(reverse=True)
# print(courses)
# print(sorted(courses))  # sorted только отображает, но не сохраняет

# print(min(nums))
# print(max(nums))
# print(sum(nums))

# print(courses.index('Math'))
# print(courses[courses.index('Math')])

# print('Math' in courses)
# print(8 in nums)

# courses_str = '*'.join(courses)
# print(courses_str)
# new_lst = courses_str.split('*')
# print(new_lst)
# print(list('Hello world'))
#
# print(courses + nums)
# print(courses * 2)

# courses2 = courses.copy()
# courses2[0] = 'Art'
# courses[1] = 'English'
# print(courses)
# print(courses2)
# print(id(courses))
# print(id(courses2))

# TUPLES
# empty_tup = ()  # объявляем кортеж tuple
# empty_tup = tuple(courses)
# print(empty_tup.index('Math'))
# print(empty_tup.count('Math'))
#
# one = (1,)  # если один элемент, нуэно поставить запятую после элемента, иначе это будет не кортеж, а строка
# print(one)
# print(type(one))

# SETS
# empty_set = set()
# print(empty_set)
# print(type(empty_set))
#
# courses.remove('Math')
# x = courses.pop()
# print(courses)
# print(x)
#
# y = ['One', 'Two', 'Three', 'One', 'Two']
# print(list(set(y)))

# courses.add('Art')
# courses.update(['Economy', 'English'])
# courses.clear()
# print(courses)

set1 = {'Math', 'History', 'Physics', 'Art'}
set2 = {'Math', 'Literature', 'Physics', 'English'}

print(set1.union(set2))
print(set1.intersection(set2))  # Выводит все общие элементы
print(set1.difference(set2))  # выводит уникальные значения для первого сета
print(set2.difference(set1))

x = [1, 2, 3]
print(bool(x))

