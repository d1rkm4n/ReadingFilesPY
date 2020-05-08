import glob
import os
import shutil


def readFile_func():
    os.chdir('C:/Users/demcdona/Desktop/1.3.46.670589.28.26540640150320180116080306069587')
    file_copy_dest = "c:/testcopy"
    for file in glob.glob('*.jpeg'):
        print(file)

readFile_func()
