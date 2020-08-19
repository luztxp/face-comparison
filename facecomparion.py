import os
import shutil
import face_recognition
import xlwt


date_dir_path='./face-1/'
date_dir_path2='./face-2/'
result_dir_path='./result/'
for file in os.listdir(date_dir_path):
    a = date_dir_path + file
    picture_of_01 = face_recognition.load_image_file(a)
    face_encoding_01 = face_recognition.face_encodings(picture_of_01)[0]
    b = file.replace('_01.jpg', '')
    c = date_dir_path2+b+'_02.jpg'
    picture_of_02 = face_recognition.load_image_file(c)
    face_encoding_02 = face_recognition.face_encodings(picture_of_02)[0]
    results = face_recognition.compare_faces([face_encoding_01], face_encoding_02,tolerance=0.6)
    face_distances = face_recognition.face_distance([face_encoding_01], face_encoding_02)
    result=b+str(face_distances)
    txt = open("./result.txt", "a").write(result+'\n')
    excel = open("./result.xlsx", "a").write(result+'\n')
    if results[0] == True:
        print("yes")
    else:
        shutil.copy(a, result_dir_path+file)
        shutil.copy(c, result_dir_path + b + "_02.jpg")