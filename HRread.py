import openpyxl
import os


def hr():
    hrbook = openpyxl.load_workbook('C:/Users/demcdona/Desktop/HRbook.xlsx', data_only=True)
    sheethr = hrbook['Sheet1']
    file = 'pyCOVID.txt'
    path = "C:/users/demcdona/desktop"

    # with open(os.path.join(path, file), 'w') as wf:
    for row in sheethr.rows:
        # wf.write(row[0].value)
        valuehr = row[0].value
        valuehr2 = row[1].value
        print(valuehr + " " + valuehr2)


hr()