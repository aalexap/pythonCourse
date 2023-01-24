# Для диапозона чисел от 0 до 100 включительно.
# Если число делится на 3 без остатка - написать число и Fizz
# Если число делится на 5 без остатка - написать число и Buzz
# Если число делится на 3 и на 5 без остатка - написать число и FizzBuzz

import time
start = time.time()

for num in range(101):
    if (num % 3 == 0):
        if (num % 5 == 0):
            print(str(num) + ' FizzBuzz')
        else:
            print(str(num) + ' Fizz')
    else:
        if (num % 5 == 0):
            print(str(num) + ' Buzz')

end = time.time() - start
print(end)
