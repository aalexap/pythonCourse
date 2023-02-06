import csv
with open('csv_files/test.csv', 'r', encoding='utf-8') as file:
    # csv_reader = csv.DictReader(file, fieldnames=['NM', 'DOB', 'TOWN'])
    # for line in csv_reader:
    #     print(line)
    csv_reader = csv.DictReader(file)

    with open('csv_files/test_copy.csv', 'w', encoding='utf-8') as wfile:
        csv_writer = csv.DictWriter(wfile, lineterminator='\n', delimiter=',', fieldnames=['Name', 'Date of birth', 'Town'])

        csv_writer.writeheader()  # пишет зоголовки
        # csv_writer.writerows(csv_reader)
        for line in csv_reader:
            for i in line:
                line[i] = line[i].upper()
            csv_writer.writerow(line)