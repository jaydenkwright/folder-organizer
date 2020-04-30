import os
import shutil
import datetime
import time
from pathlib import Path
import filetype

path = os.getcwd()
date = datetime.datetime.now()

# def create_folder(folder):
    #os.makedirs(f"{path}/downloads/{new_folder[0]}/")

def new_folder_name(kind):
    return str(kind.mime).split("/")
    

def create_folders(kind):
    new_folder = new_folder_name(kind)
    print(kind)
    if os.path.exists(f"{path}/downloads/{new_folder[0]}/"):
        print("Path exists")
    else:
        os.makedirs(f"{path}/downloads/{new_folder[0]}/")
        print(f"{path}/downloads/{new_folder[0]}/ has been created")
    if os.path.exists(f"{path}/downloads/{str(new_folder[0])}/{date.year}/"):
        print("Path exists")
    else:
        os.makedirs(f"{path}/downloads/{str(new_folder[0])}/{date.year}/")
        print(f"{path}/downloads/{str(new_folder[0])}/{date.year}/ has been created")

def move_files(path, folder, file):
    shutil.move(f"{path}/downloads/{file}", f"{path}/downloads/{folder[0]}/{date.year}/{file}")
    print(f"Moved to /downloads/{file} to {path}/downloads/{folder[0]}/{file}")
    
        

def main():
    for r, d, f in os.walk(path + "/downloads/"):
        for file in f:
            if os.path.exists(path + "/downloads/" + file):
                file_date = time.ctime(os.path.getctime(path + "/downloads/" + file))
                kind = filetype.guess(path + "/downloads/" + file)
                if kind is not(None):
                    new_folder = str(kind.mime).split("/")
                    create_folders(kind)
                    # create_folder(f"{path}/downloads/{str(new_folder[0])}/")
                    # create_folder(f"{path}/downloads/{str(new_folder[0])}/{date.year}/")
                    move_files(path, new_folder, file)
                else:
                    print('Cannot guess file type!' + file)
                    if not os.path.exists(f"{path}/downloads/others"):
                        os.makedirs(f"{path}/downloads/others")
                        print('does not exist')
                    else:
                        print('exists')
                    shutil.move(f"{path}/downloads/{file}", f"{path}/downloads/others/{file}") 
                

if __name__ == "__main__":
    main()
