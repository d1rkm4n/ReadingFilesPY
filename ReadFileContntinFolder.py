import glob
import os
import shutil
import re


def readFile_func():
    folder_path = 'C:/test'
    # copy_destination = 'C:/Users/demcdona/Desktop/InputDelBackup'
    folder = 'folder0'

    x = glob.glob('c:/test/*.xml')

    for filename in x:
        with open(filename, 'r') as f:
            if os.path.isfile(filename):
                text = f.read()
                res = str(text.strip().split())
                if 'studydescription' in text:
                    res = text.lstrip()
                    print(res)
    # shutil.copy(filename, copy_destination)
    # os.remove(filename)

readFile_func()
