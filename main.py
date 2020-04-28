import os
from pathlib import Path
import filetype

path = os.getcwd()

for r, d, f in os.walk(path + "/downloads/"):
    for file in f:
        kind = filetype.guess(path + "/downloads/" + file)
        'print(Path(file).suffix)'
        if kind is not(None):
            split_kind = str(kind.mime).split("/")
            new_folder = split_kind[0]
            if not os.path.exists(path + "/downloads/" + str(new_folder)):
                os.makedirs(path + "/downloads/" + str(new_folder))
                print('does not exist')
            else:
                print('exists')
            
            

        else:
            print('Cannot guess file type!' + file)
            if not os.path.exists(path + "/downloads/others"):
                os.makedirs(path + "/downloads/others")
                print('does not exist')
            else:
                print('exists')