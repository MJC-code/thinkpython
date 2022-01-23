import os

def walk(dirname):
    for path, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(path, filename))

walk('..')
