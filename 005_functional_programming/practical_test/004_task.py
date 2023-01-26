# Пользователь вводит некоторый произвольный список list. Написать программу, выводящую элементы списка
# в обратном порядке.

filled_lst = (input('Please enter a list of values separated by space: '))

filled_lst = filled_lst.split()
filled_lst = filled_lst[::-1]

for x in filled_lst:
    print(x)
