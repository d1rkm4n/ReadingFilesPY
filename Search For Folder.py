import os
import xlwt

folder = '//cvispacs/k$/archive/drive/lumedx/original studies'
searchfor = '1.3.46.670589.28.96161007149620140723183714449115'

# folder = 'c:/test'
# searchfor = 'folder0'

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('python')
font0 = xlwt.Font()
font0.name = 'Arial'
font0.bold = True
font0.height = 240

first_col = sheet.col(0)
first_col.width = 500 * 20
second_col = sheet.col(1)
second_col.width = 256 * 20
# third_col = sheet.col(2)
# third_col.width = 256 * 20
# forth_col = sheet.col(3)
# forth_col.width = 256 * 20
# fifth_col = sheet.col(4)
# fifth_col.width = 256 * 20

style0 = xlwt.XFStyle()
style0.font = font0

sheet.write(0, 0, "File Name", style0)
sheet.write(0, 1, "Size", style0)


# sheet.write(0, 2, "Destination", style0)
# sheet.write(0, 3, "Port", style0)
def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"


def read_file_func(path, searchfor):
    depth = 1
    row = 0

    stuff = os.path.abspath(os.path.expanduser(os.path.expandvars(path)))

    for root, dirs, files in os.walk(stuff):
        if root[len(stuff):].count(os.sep) < depth:
            for f in dirs:
                x = os.path.basename(f)
                y = (os.path.join(root, f))

                folder_size = sum(os.path.getsize(os.path.join(dirpath, filename)) for dirpath, dirnames, filenames in
                                  os.walk(y)
                                  for filename in filenames)
                folder_size_format = get_size_format(folder_size)
                if searchfor in x:
                    print('Folder Found:', x, '\nFolder size:', folder_size_format,'\nPath:', y)
                    dirs[:] = []
                    row += 1
                    sheet.write(row, 0, x)
                    sheet.write(row, 1, folder_size_format)
                    sheet.write(row, 2, y)
                    wbk.save('folderfound.xls')


read_file_func(folder, searchfor)


