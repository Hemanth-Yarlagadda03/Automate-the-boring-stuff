

import os
import re
import shutil
folderpath=input()

os.chdir(folderpath)
path = os.getcwd()

prefix_regex = re.compile(r'(Spam)(\d{,3})')

i = 1
for file in os.listdir():
    a = prefix_regex.search(file)
    if a:
        prevname= os.path.abspath(file)
        new_suffix = a.group(1) + str(i).zfill(3) + '.txt'
        newname = os.path.join(path, new_suffix)
        i += 1
        shutil.move(prevname, newname)