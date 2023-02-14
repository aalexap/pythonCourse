import csv
with open('csv_files/2019.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    i = 10
    while True:
        try:
            user_choice = int(input(f"Please select what you want to do or to know:\n0. Exit\n"
                                    f"1. Change the number of output results (current value {i})\n"
                                    f"2. Show top {i} countries by Score\n3. Show top {i} countries by GDP per capita\n"
                                    f"4. Show top {i} countries by Social support\n"
                                    f"5. Show top {i} countries by Healthy life expectancy\n"
                                    f"6. Show top {i} countries by Freedom to make life choices\n"
                                    f"7. Show top {i} countries by Generosity\n"
                                    f"8. Show top {i} countries by Perceptions of corruption\n "))

            if user_choice > 8:
                raise Exception

        except Exception:
            print('\nWrong input! Try again\n')
            continue

        else:
            if user_choice == 0:
                quit()

            elif user_choice == 1:
                while True:
                    try:
                        i = int(input("How many countries do you want to see?\n"))
                        break
                    except ValueError:
                        print("Enter only numbers from 1 to 156")

            else:
                cat = {}
                for line in csv_reader:
                    cat[float(line[user_choice])] = line[1]

                keys_list = sorted(cat.keys(), reverse=True)
                for key in keys_list[0:i]:
                    print(cat.get(key))
                print('')


#     CSV reader
#     happiness_data = list(csv.reader(file))
#     next(happiness_data)
#     happiness_data = list(happiness_data)
#
# analysis_data = []
# for line in happiness_data:
#     analysis_data.append([line[3], line[1]])
#
# analysis_data.sort(reverse=True)
#
# result = []
# for line in analysis_data:
#     if analysis_data.index(line) > 9:
#         break
#     result.append(line)
#
# for line in result:
#     print(line[1], line[0])
#
#     happines_data = csv.DictReader(file)
#     next(happines_data)
#     happines_data = list(happines_data)
#
# analysis_data = []
# for line in happines_data:
#         analysis_data.append([line['GDP per capita'], line['Country or region']])
#
# analysis_data.sort(reverse=True)
#
# result[]
# for line in analysis_data;
#     if analysis_data.index(line) > 9:
#         break
#     result.append(line)
#
# for line in result:
#     print(line[1], line[0])


# Lambda
#     happines_data = csv.reader(file)
#     next(happines_data)
#     happines_data = list(happines_data)
#
# happines_data.sort(reverse=True, key=lambda value: value[3])
#
# for line in happines_data:
#     if happines_data.index(line) < 9:
#         print(line)