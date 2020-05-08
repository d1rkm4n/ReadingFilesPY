import openpyxl
import pandas as pd
import os

hr=pd.read_csv('C:/users/demcdona/desktop/hrbook.csv')
athena= pd.read_csv('C:/users/demcdona/desktop/athena users.csv')

# print(hr.fn.isin(athena.fn))
for
if hr.fn.isin(athena.fn) is True:
    r = hr.fn.isin(athena.fn)
    print(r)
else:
    print('no')

# print(compare)
# print(athena.columns)




# def compare(x, y):
#     for x in y:
#         print(x + "- x value" + y + "- y value")
#
#     #     if x in y:
#     #         print('yes'+ x + y)
#     #     else:
#     #         print('no')
#
#
# def athena():
#     global valueathena
#     athenabook = openpyxl.load_workbook('C:/Users/demcdona/Desktop/Athenausers.xlsx')
#     sheet = athenabook['athena users']
#     file = 'pyCOVID.txt'
#     path = "C:/users/demcdona/desktop"
#
#     # with open(os.path.join(path, file), 'w') as wf:
#     for row in sheet.rows:
#         # wf.write(row[0].value)
#         valueathena = row[2].value + " " + row[3].value
#     return valueathena
#
#
# # athena()
#
#
# def hr():
#     global valuehr
#     hrbook = openpyxl.load_workbook('C:/Users/demcdona/Desktop/HRrequests.xlsx')
#     sheet = hrbook['HR Access Requests']
#     file = 'pyCOVID.txt'
#     path = "C:/users/demcdona/desktop"
#
#     # with open(os.path.join(path, file), 'w') as wf:
#     for row in sheet.rows:
#         # wf.write(row[0].value)
#         valuehr = row[1].value + " " + row[3].value
#         # value2 = row[3].value
#         # print(valuehr)
#     return valuehr
#
#
# #
#
# compare(hr(valuehr), athena())
