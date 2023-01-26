# Пользователь вводит длины трех сторон треугольника(a, b, c)[тип float].Напишите рограмму, которая
# проверяет, является ли треугольник прямоугольным(с2=a2 + b2)

side_a = float(input('Please enter side A: '))
side_b = float(input('Please enter side B: '))
side_c = float(input('Please enter side C: '))

if side_c ** 2 == side_a ** 2 + side_b ** 2:
    print('This triangle is rectangular')
else:
    print('This triangle is not rectangular')
