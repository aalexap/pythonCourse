import csv
import sys

with open('csv_files/test.csv', 'r', encoding='utf-8') as csv_file:
    # x = [1, 2, 3, 4, 5]
    # y = iter(x)

    # csv_reader = csv.reader(csv_file)
    # print(csv_reader)
    # col_names = next(csv_reader)
    # for line in csv_reader:
    #     print(line)

    # csv_reader = list(csv.reader(csv_file))
    # print(csv_reader)

    csv_reader = csv.reader(csv_file)

    with open('csv_files/test_copy.csv', 'w', encoding='utf-8') as new_file:
        csv_writer = csv.writer(new_file, delimiter='.', lineterminator='\n', quotechar='*', quoting=csv.QUOTE_ALL)

        for line in csv_reader:
            csv_writer.writerow(line)

    with open('csv_files/test_copy.csv', 'r', encoding='utf-8') as new_file:
        csv_reader = csv.reader(new_file,  delimiter='.', quotechar='*')
        for x in csv_reader:
            print(x)