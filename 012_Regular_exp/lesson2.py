import re

with open('people.txt', 'r', encoding='utf-8') as file:
    people_data = file.read()

phones = []
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
matches = pattern.finditer(people_data)

for match in matches:
    phones.append(match.group())

phones.sort()
print(phones)
