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
                                    f"7. Show top {i} countries byGenerosity\n"
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
                social_support = {}
                for line in csv_reader:
                    social_support[float(line[user_choice])] = line[1]

                keys_list = sorted(social_support.keys(), reverse=True)
                for key in keys_list[0:i]:
                    print(social_support.get(key))
