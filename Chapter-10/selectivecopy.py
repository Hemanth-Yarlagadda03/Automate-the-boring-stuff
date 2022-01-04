import os
import shutil


folder = input()

extension = input()

destination = input()

for folders, subfolders, filenames in os.walk(folder):

        for filename in filenames:

            if filename.endswith('{}'.format(extension)):
                shutil.copy(os.path.join(folders, filename), destination)

print('Files copied from' ,os.path.basename(folder), 'to',
      os.path.basename(destination))