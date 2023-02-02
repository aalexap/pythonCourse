# Написать программу которая открывает текстовый файл и считает следующее:
# 1. Общее кол-во слов
# 2. Кол-во уникальных (разных)
#
# Не влияет на уникальность:
# Заглавные и прописные буквы
# Знаки препинания: ',' '.' '!' '?'
#
# Сохраняет кол-ва в отдельный файл.
# Выписывает все уникальные слова в алфавитном порядке.

with open('text_files/trimushketera.txt', 'r', encoding='UTF8') as file:
    data = file.read()
    list1 = data.split()
    num_words = len(list1)
    # print('Number of words in book :', num_words)

    data = data.lower()
    data = data.replace(',', '')
    data = data.replace('.', '')
    data = data.replace('!', '')
    data = data.replace('?', '')

    list2 = data.split()
    list2 = set(list2)
    # print(len(list2))

    with open(f'text_files/result.txt', 'w', encoding='utf-8') as result:
        result.write('\nNumber of words in book: ')
        result.write(str(num_words))
        result.write('\nNumber of uniq words in book: ')
        result.write(str(len(list2)))



    list2 = list(list2)
    list2.sort()

    for x in list2:
        print(x)
