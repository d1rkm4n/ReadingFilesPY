from tkinter import *
import re
import xlwt

File = open('c:/test/PPHSTEST6_NetConfig', 'r')
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('python')
host = 'HOST '
process = 'PROCESSNAME'
dest = 'DEST'
port = 'PORT '

font0 = xlwt.Font()
font0.name = 'Arial'
font0.bold = True
font0.height = 240

first_col = sheet.col(0)
first_col.width = 400 * 20
second_col = sheet.col(1)
second_col.width = 400 * 20
third_col = sheet.col(2)
third_col.width = 400 * 20
forth_col = sheet.col(3)
forth_col.width = 400 * 20
fifth_col = sheet.col(4)
fifth_col.width = 400 * 20

style0 = xlwt.XFStyle()
style0.font = font0

sheet.write(0, 0, "Processname", style0)
sheet.write(0, 1, "Host", style0)
sheet.write(0, 2, "Destination", style0)
sheet.write(0, 3, "Port", style0)


def read_file_func():
    stopwords = {'MQSPORT','ICLSERVERPORT','FTPPORT ftp','PROCESSNAME template'}
    row = 0
    col = 0
    for line in File:
        if process in line or host in line or port in line or dest in line:
            res = " ".join(re.findall("[\d\w.]+", str(line.strip().split())))
            if port in res:
                row += 1
                # res3 = " ".join(re.findall("[\d\w.]+", str(line.strip().split())))
                if res not in stopwords:
                    print(res)
                    sheet.write(row, 3, res)
            if host in res:
                # res3 = " ".join(re.findall("[\d\w.]+", str(line.strip().split())))
                if res not in stopwords:
                    print(res)
                    sheet.write(row, 2, res)
                    wbk.save('reformattedjoe.data.xls')
            # if process in res:
            #     # res3 = " ".join(re.findall("[\d\w.]+", str(line.strip().split())))
            #     if res not in stopwords:
            #         print(res)
            #         sheet.write(row, 1, res)
            #         wbk.save('reformattedjoe.data.xls')
            if dest in res:
                # res3 = " ".join(re.findall("[\d\w.]+", str(line.strip().split())))
                if res not in stopwords:
                    print(res)
                    sheet.write(row, 0, res)
                    wbk.save('reformattedjoe.data.xls')

        #     if res not in stopwords:
        #         print(res)
        #         sheet.write(row, 0, res)
        # #
        # if host in line:
        #     res1 = " ".join(re.findall("[\d\w.]+", str(line.strip().split())))
        #     print(res1)
        #     sheet.write(row, 1, res1)
        #
        # if dest in line:
        #     res2 = " ".join(re.findall("[\d\w.]+", str(line.strip().split())))
        #     print(res2)
        #     sheet.write(row, 2, res2)

        # if port in line:
        #     res3 = " ".join(re.findall("[\d\w.]+", str(line.strip().split())))
        #     if res3 not in stopwords:
        #         print(res3)
        #         sheet.write(row, 3, res3)
        #         wbk.save('reformattedjoe.data.xls')
        #         row += 1

read_file_func()
