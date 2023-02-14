import os
import time
import sys

# os.rename('sample.txt', 'temp/sample.txt')
# # os.rename('sample.txt', 'sample.txt')

# os.remove('sample.txt')
# os.rmdir('temp')

# print(os.stat('sample.txt').st_size)

# info = os.walk('../')
# for dirpath, dirnames, filenames in info:
#     if '.git' in dirpath or '.idea' in dirpath:
#         pass
#     else:
#         print('Current dir: ' + dirpath)
#         print('Directories: ' + str(dirnames))
#         print('Files: ' + str(filenames))
#         if 'lesson.py' in filenames:
#             print('*' * 20)
#             print(dirpath)
#             print('*' * 20)
#         print()


# print(os.environ.get('USERNAME'))


file_path = os.path.join('C:\\home', 'sample.txt')
print(file_path)
print(sys.getsizeof(file_path))  # библиотека sys для работы с файлами - вес, размер и т.д.
print(os.path.basename('/somedir/dir10/sample.txt'))
print(os.path.dirname('/somedir/dir10/sample.txt'))
print(os.path.split('/somedir/dir10/sample.txt'))
print(os.path.splitext('/somedir/dir10/sample.txt'))

print(os.path.exists('../013_itertools_module'))

print(os.path.isdir('../013_itertools_module'))
print(os.path.isfile('../013_itertools_module/lesson.py'))