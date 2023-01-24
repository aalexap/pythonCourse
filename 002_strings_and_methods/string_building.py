# a = 'Hello'
# b = 'World'
#
# print(a, b, 12321, True, None, sep='***', end='')
# txt = 'Hello\nWorld'
# print(txt)
#
# print("that's")
# print('that\'s')
# print('test\\\'')
#
# print(""" "Metro
#
# 2033""")

salary = 2000
name = 'John'
age = 25
txt = '{0}s salary is {1}. He is {2} years old.'
print(txt.format(name, salary, age))

product = 'computer'
price = 1000
txt2 = 'This {p:} costs {pr:.2f} EUR'
print(txt2.format(p=product, pr=price))

x = 1234.12312312312
y = 123.1233
print('The value of x is %4f' % x)

emp_name = 'John'
emp_age = 15
emp_salary = 1000
# emp_string ='Hi my name is %(name)s! I am %(age)s years old, My salary is %(salary).2f' %{'name': emp_name, 'salary': emp_salary, 'age': emp_age}
# print(emp_string)

print(f'Hi, my name is {emp_name.upper()}. I am {emp_age + 10} years old. My salary is {emp_salary:.2f} ')
