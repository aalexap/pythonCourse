courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', 'Math']

for course in courses:
    if course == 'Math':
        print('I don\'t like Math!')
    else:
        print(course.upper())

pairs = [['JAak', 'Smith', 22], ['Mary', 'Gold', 25], ['Bob', 'Summers', 35]]
for first, last, age in pairs:
    print(f'Hello {first} {last}. You are {age} years old!')

# for num1 in range(10):  # range (от, до, шаг)
#     for num2 in range(10):
#         for num3 in range(10):
#             for num4 in range(10):
#                  print(num1, num2, num3 ,num4)

print(list(range(10)))

