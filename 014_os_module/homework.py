import os

def rep(filename, extension):
    os.replace(filename, extension + '/' + filename)


os.chdir('needs_sorting')
i = 0
for filename in os.listdir():
    if os.path.isfile(filename):
        i += 1
        extension = os.path.splitext(filename)[1][1:]
        if os.path.isdir(extension):
            rep(filename, extension)
        else:
            os.mkdir(extension)
            rep(filename, extension)
print(f'{i} files were found and moved')
