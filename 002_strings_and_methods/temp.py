string_sample1 = 'Hello world world'
string_sample2 = 'first letteR is lowErcase. Hello'
string_sample3 = ' extra whitespaces    *    '
german_sample = 'der Fluß'

# [START:END:STEP] - END not included
print(string_sample1[-1])
print(string_sample1[6:11])
print(string_sample1[-6:])
print(string_sample1[::2])
print(string_sample1[::-1])

# len - length of string
print(len(string_sample1))
print(string_sample1[len(string_sample1) - 1])

print(string_sample1.upper())
print(german_sample.lower())
print(german_sample.casefold())

print(string_sample1.isupper())
print(string_sample1.islower())

print(string_sample2.capitalize())
print(string_sample2.title())

# strip - удаляет все пробелы в начале и в конце строки, или символы указанные в скобках
print(string_sample3.strip())
print(string_sample3.strip('* '))
print(string_sample3.rstrip('* '))
print(string_sample3.lstrip('* '))


print(string_sample1.replace('world', 'planet', 1))
print(string_sample1.replace(' ', '').replace('o', ''))

print(string_sample1.split())

# a, b, c = string_sample1.split()
# print(a)
# print(b)
# print(c)

# a, b, c = input('Please enter: ').split()
# print(a)
# print(b)
# print(c)

# count - считает кол-во определенный символов или выражений
print(string_sample1.count('world', 7, 17))
# find - находит символ с которого начинается заданное значение
print(string_sample1.find('world', 7))

print('world' in string_sample1)
