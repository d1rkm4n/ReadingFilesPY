import glob
import os
import shutil


# from tkinter import *


# def window_function():
#     pass
#     m = Tk()
#     m.title("Read Files")
#     Label(m, text='Folder Path').grid(row=0)
#     Label(m, text='Last Name').grid(row=1)
#     e1 = Entry(m)
#     e2 = Entry(m)
#     e1.grid(row=0, column=1)
#     e2.grid(row=1, column=1)
#     m.mainloop()
#
#     print(e1)
#     print(e2)


def readFile_func():
    folder_path = 'C:/test'
    top_dir = os.listdir(folder_path)
    # copy_destination = 'C:/Users/demcdona/Desktop/InputDelBackup'
    folder = 'folder0'
    for filename in folder_path:
        with open(filename, 'r') as f:
            text = f.read()
            print(text)
    # shutil.copy(filename, copy_destination)
    # os.remove(filename)

    # else:
    #     print('false')
    # for name in top_dir:
    #     if os.path.isdir(os.path.join(folder_path, name)):
    #         f = (os.path.join(folder_path, name, folder))
    #         if os.path.isdir(f):
    #             print(f)
    #             break

                # with open(f, 'r') as x:
                #     text = x.read()
                #     print(text)

                # print(f)

            # for file in os.listdir(os.path.join(base, name)):
            #     if os.path.isfile(os.path.join(base, name, file)):
            #         print(os.path.join(base, name, file))


readFile_func()
