# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r+' - read and write

# file = open('text_files/lorem.txt')
# file = open(r'text_files/lorem.txt', 'r', encoding='utf-8')  # r' - сырая строка снимает форматирование, не подставить переменные. encoding cp-1257 - Baltic Windows
# print(file.name)
# print(file.mode)
# print(file.encoding)
# print(file.closed)
# file.close()
# print(file.closed)

# with open(r'text_files/lorem.txt', 'r', encoding='utf-8') as file:
    # data = file.read()

    # print(data)
    # data = file.readlines()
    # data = file.readline()

    # chunk = 1000
    # data = file.read(chunk)
    # while len(data):
    #     print(data)
    #     data = file.read(chunk)

    # data = file.read()
    # print(len(data))
    # file.seek(0)
    # data = file.read()
    # print(len(data))

# import datetime
# dt = datetime.date.today()
# with open(f'text_files/tester{dt}.txt', 'w', encoding='utf-8') as file:
#     file.write('Hello planet!\n')
#     file.write('Hello world!\n')
#     file.write(str(123123))
    # file.seek(0)
    # file.write('*****')

# with open('text_files/lorem.txt', 'r', encoding='utf-8') as read_file:
#     data = read_file.read()
#     with open(f'text_files/tester.txt', 'w', encoding='utf-8') as file:
#         file.write(data.upper())


# with open(f'text_files/tester123.txt', 'x', encoding='utf-8') as file:
#     file.write('Hello planet!')

# with open(f'text_files/tester123.txt', 'r+', encoding='utf-8') as file:
#     data = file.read()
#     print(data)
#     data2 = file.read()
#     file.seek(0)
#     file.write(data.upper())

with open('text_files/img.jpg', 'rb') as file:
    with open('text_files/img_copy.jpg', 'wb') as wfile:
        data = file.read(28096)
        while len(data) > 0:
            wfile.write(data)
            data = file.read(28096)

        wfile.write(data)