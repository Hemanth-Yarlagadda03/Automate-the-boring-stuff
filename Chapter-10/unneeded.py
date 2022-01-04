

import send2trash
import os

dir_search = input()
os.chdir(dir_search)
dir_search = os.path.abspath('.')

for folder_name, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        filename = os.path.join(folder_name, filename)
        size = os.path.getsize(filename)
        if size > 100000000:
            print(os.path.abspath(filename) + ' - ' + str(size))
            send2trash.send2trash(filename)


