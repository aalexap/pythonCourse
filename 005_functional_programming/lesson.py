# def no_parameters():
#     # print('Hello world!')
#     return 'Hello world!'
#
#
# def squares(number1, number2):
#     return number1 ** number2
#     # if number < 0:
#     #     return number ** 3  # return приводит к окончанию работы функции
#     # else:
#     #     return number ** 2
#
# def print_message(name, age, profession):
#     print(f'Hello {name}. You are {age} years old. You work as {profession}.')
#
# print(no_parameters())
# print(squares(5, 3))
# print_message('Aleksei', 36, 'busenesman')
# people = [('Roman', 34, 'Lector'), ('Jack', 25, 'Mechanic')]
# for person in people:
#     print_message(person[0], person[1], person[2])


# def tester():
#     a = 10
#     b = 20
#     print(a, b, c)
#     return(a, b, c)
#
# a = 1
# b = 2
# c = 3
# print(a, b, c)
# x = tester()
# print(x)


# def test123(a, b, d, c=1):
#     return a * b * c * d
#
#
# print(test123(10, 5, 3))
# print(test123(5, d=3, b=5))


# def tester(a, b=1, *args, **kwargs):
#     print(a, b)
#     print(args)
#     for arg in args:
#         print(arg)
#     print(kwargs)
#
#
# tester(1,1, 'hello', 123, True, False, None, 0.123, 'hello again!', name='Roman', age=34)


# def say_hello():
#     print('Hello')
#
#
# def take_name(name):
#     say_hello()
#     print(name)
#
#
# take_name('Aleksei')
#
#
# def wrapper(f):
#     print('Starting work')
#     f()
#     print('Ending work')
#
#
# wrapper(say_hello)


# import funcs
# print(funcs.double(4))

from funcs import double as dbl
# print(double(5))
print(dbl(123))


