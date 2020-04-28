import os
import shutil
import datetime
import time
from pathlib import Path
import filetype

path = os.getcwd()
date = datetime.datetime.now()

def create_folder(folder):
    if os.path.exists(path):
        print("path exists")
    else:
        os.makedirs(path)
        print("Path created")



for r, d, f in os.walk(path + "/downloads/"):
    for file in f:
        if os.path.exists(path + "/downloads/" + file):
            file_year = time.ctime(os.path.getctime(path + "/downloads/" + file))
            kind = filetype.guess(path + "/downloads/" + file)
            if kind is not(None):
                new_folder = str(kind.mime).split("/")
                create_folder(f"{path}/downloads/{str(new_folder[0])}/")
                create_folder(f"{path}/downloads/{str(new_folder[0])}/{date.year}/")
                shutil.move(f"{path}/downloads/{file}", f"{path}/downloads/{new_folder[0]}/{date.year}/{file}")
                print(f"Moved to /downloads/{file} to {path}/downloads/{new_folder[0]}/{file}")
            else:
                print('Cannot guess file type!' + file)
                if not os.path.exists(f"{path}/downloads/others"):
                    os.makedirs(f"{path}/downloads/others")
                    print('does not exist')
                else:
                    print('exists')
                shutil.move(f"{path}/downloads/{file}", f"{path}/downloads/others/{file}") 
        else:
            print(f'{file} is not in root directory')