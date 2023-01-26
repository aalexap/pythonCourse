while True:
    try:
        user_id = input('Please enter id code: ')
        int(user_id)
        if len(user_id) != 11:
            raise Exception
    except ValueError:
        print('Code you entered is not numeric.')
        continue
    except Exception:
        if len(user_id) > 11:
            print('Code is to long!')
        else:
            print('Code is to short!')
        continue
    else:
        error_msg = ('You have entered a wrong code, please double-check and re-enter it')
        # Defining a century
        if int(user_id[0]) == 1 or int(user_id[0]) == 2:
            century = 1800
        elif int(user_id[0]) == 3 or int(user_id[0]) == 4:
            century = 1900
        elif int(user_id[0]) == 5 or int(user_id[0]) == 6:
            century = 2000
        elif int(user_id[0]) == 7 or int(user_id[0]) == 8:
            century = 2100
        else:
            print(error_msg)
            continue

        # Defining sex
        if int(user_id[0]) % 2 == 0:
            sex = 'woman'
        else:
            sex = 'man'

        # determine the year of birth
        birthday_year = century + int(user_id[1:3])

        # determine the month of birth
        if int(user_id[3:5]) > 0 and int(user_id[3:5]) <= 12:
            birthday_month = int(user_id[3:5])
        else:
            print(error_msg)
            continue

        # Determining a birthday
        birthday_day = int(user_id[5:7])
        if birthday_month in {1, 3, 5, 7, 8, 10, 12} and birthday_day > 0 and birthday_day <= 31:
            pass
        elif birthday_month in {4, 6, 9, 11} and birthday_day > 0 and birthday_day <= 30:
            pass
        elif birthday_month == 2 and birthday_day > 0 and birthday_day <= 29:
            pass
        else:
            print(error_msg)
            continue

        # Determining the place of birth
        if birthday_year < 2013:
            if int(user_id[7:10]) >= 0 and int(user_id[7:10]) <= 10:
                place = ('in Kuressaare haigla')
            elif int(user_id[7:10]) >= 11 and int(user_id[7:10]) <= 19:
                place = ('in Tartu Ülikooli Naistekliinik')
            elif int(user_id[7:10]) >= 21 and int(user_id[7:10]) <= 150:
                place = ('in Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)')
            elif int(user_id[7:10]) >= 151 and int(user_id[7:10]) <= 160:
                place = ('in Keila haigla')
            elif int(user_id[7:10]) >= 161 and int(user_id[7:10]) <= 220:
                place = ('in Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)')
            elif int(user_id[7:10]) >= 221 and int(user_id[7:10]) <= 270:
                place = ('in Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)')
            elif int(user_id[7:10]) >= 271 and int(user_id[7:10]) <= 370:
                place = ('in Maarjamõisa kliinikum (Tartu), Jõgeva haigla')
            elif int(user_id[7:10]) >= 371 and int(user_id[7:10]) <= 420:
                place = ('in Narva haigla')
            elif int(user_id[7:10]) >= 421 and int(user_id[7:10]) <= 470:
                place = ('in Pärnu haigla ')
            elif int(user_id[7:10]) >= 471 and int(user_id[7:10]) <= 490:
                place = ('in Haapsalu haigla')
            elif int(user_id[7:10]) >= 491 and int(user_id[7:10]) <= 520:
                place = ('in Järvamaa haigla (Paide)')
            elif int(user_id[7:10]) >= 521 and int(user_id[7:10]) <= 570:
                place = ('in Rakvere haigla, Tapa haigla')
            elif int(user_id[7:10]) >= 571 and int(user_id[7:10]) <= 600:
                place = ('in Valga haigla')
            elif int(user_id[7:10]) >= 601 and int(user_id[7:10]) <= 650:
                place = ('in Viljandi haigla')
            elif int(user_id[7:10]) >= 651 and int(user_id[7:10]) <= 700:
                place = ('in Lõuna-Eesti haigla (Võru), Põlva haigla ')
            else:
                place = ('not in Estonia')
        else:
            place = ('')

        # reference value check
        check = int(user_id[0]) * 1 + int(user_id[1]) * 2 + int(user_id[2]) * 3 + int(user_id[3]) * 4\
                 + int(user_id[4]) * 5 + int(user_id[5]) * 6 + int(user_id[6]) * 7 + int(user_id[7]) * 8\
                 + int(user_id[8]) * 9 + int(user_id[9]) * 1
        control = check % 11

        if (control < 10 and control != int(user_id[10])) or control > 10:
             print(error_msg)
             continue
        elif control == 10:
            check = int(user_id[0]) * 3 + int(user_id[1]) * 4 + int(user_id[2]) * 5 + int(user_id[3]) * 6 \
                    + int(user_id[4]) * 7 + int(user_id[5]) * 8 + int(user_id[6]) * 9 + int(user_id[7]) * 1 \
                    + int(user_id[8]) * 2 + int(user_id[9]) * 3
            control = check % 11
            if (control < 10 and control != int(user_id[10])) or (control > 10) or \
                    (control == 10 and (int(user_id[10]) != 0)):
                print(error_msg)
                continue

        # check the date of birth against the current date
        from datetime import date
        today = date.today()
        birthday = date(birthday_year, birthday_month, birthday_day)
        if birthday > today:
            print('Apparently this person has not yet been born')
            break

        import calendar

        print('The personal code', user_id, 'you have entered, belongs to a', sex, 'born on',
              calendar.month_name[birthday_month], str(birthday_day) + ',', str(birthday_year) + '.')
        if birthday_year < 2013:
            print('It is likely that this', sex, 'was born', place)
        break
