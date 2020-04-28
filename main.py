import os
from pathlib import Path
import filetype

path = os.getcwd()

for r, d, f in os.walk(path + "/downloads/"):
    for file in f:
        kind = filetype.guess(path + "/downloads/" + file)
        'print(Path(file).suffix)'
        if kind is None:
            print('Cannot guess file type!')

        print(str(kind.mime))