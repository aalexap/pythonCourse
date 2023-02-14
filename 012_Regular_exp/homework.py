'''1. Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF, то есть # и содержит затем 6 шестнадцатеричных символов.
	HASH цвета используют значения от 0 до 15, где 0-9 цифры от нуля до 9, 10-15 буквы от A-F.

2. Создать запрос для определения в тексте цифр, за которыми не стоит знак +. (Примеры выражений “2*9-6*5” или (3+5)-9*4)

3. Найти в тексте время. Время имеет формат часы:минуты. И часы, и минуты состоят из двух цифр, пример: 09:00. Напишите регулярное выражение для поиска времени в строке: «Завтрак в 09:00». Учтите, что «37:98» – некорректное время.
(25:00, 12:82, 123:23, 23:232, 123:123)

4. Написать программу котороая будет выбирать из файла people.txt:
	1) Все имена и фамилии
	2) Все адреса

5. Написать регулярное выражение для проверки строки, задача определить состоит ли строка только из символов a-z, A-Z, 0-9.

6. Написать регулярное выражение для определения эстонского личного кода (isikukood)

Все строки произвольные.'''

import re

# # 1 Hash colors (#FFFFFF)
# sample = '#1239af'
# pattern = re.compile(r'#[0-9A-F]{6}',re.I)
# print(pattern.findall(sample))
#
# # 2
# sample = '345-12312+123123+12312-23234*234234-123'
# pattern = re.compile(r'(\d+)[^+\d]|(\d+$)')
# matches = pattern.finditer(sample)
# for match in matches:
#     print(match.group(1) or match.group(2))

# # 3
# sample = '14:20, 30:13, 13:90, 123:23, 21:213:123:123, 13:24'
# pattern = re.compile(r'\b([01][0-9]|2[0-3]):([0-5][0-9])\b')
# matches = pattern.finditer(sample)
# for match in matches:
#     print(match)

# 4
# with open('people.txt', 'r', encoding='utf-8') as file:
#     data = file.read()
#
# name_pattern = re.compile(r'([A-Za-z]+ [A-Za-z-]+)\n')
# address_pattern = re.compile(r'\d{3} [0-9A-Za-z\'-]+ St\., [A-Za-z\'-]+ [A-Z]{2} \d{5}')
# matches1 = name_pattern.findall(data)
# print(len(matches1))
#
# matches2= address_pattern.findall(data)
# print(len(matches2))
#
# people_pairs = list(zip(matches1, matches2))
# print(list(people_pairs))
#
# people_dict = {}
# cnt=0
# for name, address in people_pairs:
#     people_dict[cnt] = {'name': name, 'address': address}
#     cnt += 1
#
# print(people_dict)

# 5
# sample = 'asdsasf2435tASDass'
#
# pattern = re.compile(r'[^A-Za-z0-9]')
# matches = pattern.findall(sample)

# if matches:
#     print(False)
# else:
#     print(True)

# if not matches:
#     print(True)
# else:
#     print(False)

# 6
sample ='38605210342'
pattern = re.compile(r'[1-8][0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{4}')
matches = pattern.finditer(sample)

for m in matches:
    print(m)