x = 5
empty_dict = {'name': 'Aleksei', 'surname': 'Aparin', 1: 'One', x: 'Five',
              'lst': [1, 2, 3, 4], 'dct': {'one': 1, 'two': 2}}
# print(empty_dict['name'])
# print(empty_dict['dct']['two'])
# print(empty_dict.get('job', 'Hello!'))  # get - на тот случай, если нет такого ключа, через запитую, что вывести, если ключа нет

empty_dict['name'] = 'Jack'
empty_dict['phone'] = '555-555-555'  # можно добавить новую пару в словарь
print(empty_dict)
empty_dict.update(name='Aleksei')  #add one
empty_dict.update({'name': 'Jack', 'surname': 'Smith', 'job': 'Programmer'})  # add any
x = empty_dict.pop('name')  # удаляет из оригинала и принимает значение ключа
del empty_dict['surname']  # удаляет, без сохранения значений
print(empty_dict)
print(x)

print(empty_dict.keys())
print(empty_dict.values())
print(empty_dict.items())

for key, val in empty_dict.items():
    print()
    print(key)
    print(val)
    print()



