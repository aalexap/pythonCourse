x = 0
if x > 0:
    print('X is a positive number')
elif x < 0:
    print('X is negative number')
else:
    print('X is a zero')

print('Good bye!')


idcode = '386050342'
if len(idcode) == 11:
    print('ID is valid')
else:
    if len(idcode) > 11:
        print('Code is to long!')
    else:
        print('Code is to short!')

y = 6
if y > 0:
    print('Y is greater than 0')
if y > 5:
    print('Y is greater than 5')
if y > 9:
    print('Y is greater than 9')
