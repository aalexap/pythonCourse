# 1 Написать программу, запрашивающую имя, фамилию и возраст пользователя и выводящую строку вида:
#         Hello, <Фамилия пользователя> <Имя пользователя>. Your age is: <возраст>

name = input('Please enter your name: ')
surname = input('Please enter your surname: ')
age = input('Please enter your age: ')
print(f'Hello, {surname} {name}. Your age is: {age}')
