import os
import shutil
from pathlib import Path
import filetype

path = os.getcwd()

for r, d, f in os.walk(path + "/downloads/"):
    for file in f:
        if os.path.exists(path + "/downloads/" + file):
            'print(file)'
            kind = filetype.guess(path + "/downloads/" + file)
            'print(Path(file).suffix)'
            if kind is not(None):
                new_folder = str(kind.mime).split("/")
                if os.path.exists(path + "/downloads/" + str(new_folder[0])):
                    print("exists")
                    if file:
                        shutil.move(path + "/downloads/" + file, path + "/downloads/" + new_folder[0] + "/" + file)
                        print("Moved to /downloads/" + file, path + "/downloads/" + new_folder[0] + "/" + file)
                else:
                    os.makedirs(path + "/downloads/" + str(new_folder[0]))
                    print('does not exist')
            else:
                print('Cannot guess file type!' + file)
                if not os.path.exists(path + "/downloads/others"):
                    os.makedirs(path + "/downloads/others")
                    print('does not exist')
                else:
                    print('exists')
    else:
        print('file does not exist')