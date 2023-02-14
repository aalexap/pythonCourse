import os

os.chdir('needs_sorting')
i = 0
for filename in os.listdir():
    if os.path.isfile(filename):
        i += 1
        extension = os.path.splitext(filename)[1][1:]
        if os.path.isdir(extension):
            os.replace(filename, extension + '/' + filename)
        else:
            os.mkdir(extension)
            os.replace(filename, extension + '/' + filename)
print(f'{i} files were found and moved')
