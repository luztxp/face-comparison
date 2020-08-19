import xlrd
import os
import shutil
FileContactList = "./test.xls"
FileName = FileContactList
src_dir_path = './xuehao'
target_dir_path = './xtos'
for file in os.listdir(src_dir_path):
 c = file.replace('.jpg', '')
 KeyStr = c
 FileObj = xlrd.open_workbook(FileName)
 sheet = FileObj.sheets()[0]
 row_count = sheet.nrows
 col_count = sheet.ncols
 for element in range(row_count):
    if KeyStr.lower() in (str(sheet.row_values(element))).lower():
        print()
        a=sheet.row_values(element)
        b=a[1]
        shutil.copy(src_dir_path + '/' + file, target_dir_path + '/' + b +".jpg")