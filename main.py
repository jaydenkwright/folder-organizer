import os
import shutil
import datetime
from pathlib import Path
import filetype

path = os.getcwd()
date = datetime.datetime.now()

for r, d, f in os.walk(path + "/downloads/"):
    for file in f:
        if os.path.exists(path + "/downloads/" + file):
            kind = filetype.guess(path + "/downloads/" + file)
            if kind is not(None):
                new_folder = str(kind.mime).split("/")
                if os.path.exists(path + "/downloads/" + str(new_folder[0])):
                    print("Path exists")
                else:
                    os.makedirs(path + "/downloads/" + str(new_folder[0]))
                    print('Path created')
                if os.path.exists(f"{path}/downloads/{str(new_folder[0])}/{date.year}/"):
                    print("Path exists")
                else:
                    os.makedirs(f"{path}/downloads/{new_folder[0]}/{date.year}/")
                    print("Path Created")

                #shutil.move(path + "/downloads/" + file, path + "/downloads/" + new_folder[0] + "/" + file)
                shutil.move(f"{path}/downloads/{file}", f"{path}/downloads/{new_folder[0]}/{date.year}/{file}")
                print(f"Moved to /downloads/{file} to {path} + /downloads/ {new_folder[0]} / + {file}")
            else:
                print('Cannot guess file type!' + file)
                # if not os.path.exists(path + "/downloads/others"):
                #     os.makedirs(path + "/downloads/others")
                #     print('does not exist')
                # else:
                #     print('exists')
        else:
            print('Not in root directory' + file)