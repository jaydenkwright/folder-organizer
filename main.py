import os
from pathlib import Path
import filetype

path = os.getcwd()

for r, d, f in os.walk(path + "/downloads/"):
    for file in f:
        print(file)