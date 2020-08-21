import xlrd
import os
import shutil
import face_recognition
FileContactList = "./test.xls"
FileName = FileContactList
src_dir_path = './shenfenzheng'
src_dir_path2 = './xuehao/'
result_dir_path='./result/'
wrong_dir_path='./wrong/'
t=0
for file in os.listdir(src_dir_path):
 t=t+1
 print(t)
 c = file.replace('.jpg', '')
 KeyStr = c
 FileObj = xlrd.open_workbook(FileName)
 sheet = FileObj.sheets()[0]
 row_count = sheet.nrows
 col_count = sheet.ncols
 for element in range(row_count):
    if KeyStr.lower() in (str(sheet.row_values(element))).lower():
        p=sheet.row_values(element)
        b=p[0]
        g=src_dir_path2+b+".jpg"
        if os.path.exists(g) == True:
            a = src_dir_path+"/"+file
            picture_of_01 = face_recognition.load_image_file(a)
            face_encoding_01 = face_recognition.face_encodings(picture_of_01)
            if len(face_encoding_01) > 0:
             picture_of_02 = face_recognition.load_image_file(g)
             face_encoding_02 = face_recognition.face_encodings(picture_of_02)
             if len(face_encoding_02) > 0:
               face_encoding_01 = face_recognition.face_encodings(picture_of_01)[0]
               face_encoding_02 = face_recognition.face_encodings(picture_of_02)[0]
               results = face_recognition.compare_faces([face_encoding_01], face_encoding_02, tolerance=0.6)
               face_distances = face_recognition.face_distance([face_encoding_01], face_encoding_02)
               result = c + str(face_distances)
               excel = open("./result.xlsx", "a").write(result + '\n')
               if results[0] == True:
                   print(c+"yes")
               else:
                   shutil.copy(a, result_dir_path + file)
                   shutil.copy(g, result_dir_path + c + "_2.jpg")
                   print(c+"no")
             else:
                 shutil.copy(g, wrong_dir_path +"/2w/"+ b + ".jpg")
                 print(b + "no")
            else:
                shutil.copy(a, wrong_dir_path +"/1w/"+ file)
        else:
            shutil.copy(src_dir_path+"/"+file, wrong_dir_path +"/nlu/" + file)
