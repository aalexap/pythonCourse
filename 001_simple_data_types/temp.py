a = 5
print(a)
# type - проеврка типа данных
print(type(a))  # integer (int)


b = 0.123
print(b)
print(type(b))  # float (float)

# print(help(type))

c = 'hello'
d = "Hello"
e = '''Hello'''

print(c)  # string (str)
print(type(c))
print(len(c))  # len - длина строки

true_val = True
false_val = False
print(true_val)
print(type(true_val))  # boolean (bool)

none_val = None

print(none_val)
print(type(none_val))  # NoneType
x = None

print(round(1.5))  # round - округление
print(round(2.5))


a = 200.123
b = 500
print(a + b)

str1 = 'Hello'
str2 = 'world'
print(str1 + '' + str2)

print(True + True)

print(a - b)


print(a * b)
print('*' * 20)
print(b / a)
print(b // a)
print(b % 30)  # Остаток при делении
print(b ** 2)  # Возведение в степень
print(b ** 0.5)  # извлечение корня

print(((10 + 5) * 2) ** 2)  # возведение в степень ** выполняется первее остальных


int_val = 500
float_val = 50.9
string_num_val = '123.23'
string_text_val = 'Hello world!'

print(string_text_val + str(int_val))

print(float(int_val))
print(int(float_val))

print(str(int_val))
print(type(str(int_val)))

print(int(float(string_num_val)))
print(bool(0.0))
print(bool(''))
print(bool(None))

a = 5
a = float(a)

print(type(a))


# c = input('enter first number: ')
# d = input('enter second number: ')
# c = int(c)
# d = int(d)
# print(c + d)