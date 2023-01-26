# people = [('Jack', 'Smith', 18), ('Mary', 'Gold', 20)]
#
# for person in people:
#     print(person)
#
# for name, surname, age in people:
#     print(name, surname, age)

# x = 0
# while x < 100:
#     print('I can\'t stop!', x)
#     x += 1

# dist_to_target = 1567
# current_pos = 0
#
# step = 0.6
# cnt = 0
# while current_pos < dist_to_target:
#     print(cnt)
#     current_pos += step
#     cnt += 1

# for x in range(10):
#     if x == 5:
#         continue
#     if x == 8:
#         break
#     print(x)
#
# cnt = 0
# while True:
#     print(cnt)
#     if cnt == 100:
#         break
#     cnt += 1

# try:
#     user_input = float(input('Enter number: '))
# except:
#     print('Must enter a number!')
# else:
#     print(user_input ** 2)
# finally:
#     print('Good bye!')

while True:
    try:
        user_id = input('Please enter id code: ')
        int(user_id)
        if len(user_id) != 11:
            raise Exception  # raise вызывает ошибку
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
        print('Your id code is', user_id)
        break
