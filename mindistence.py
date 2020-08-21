import os
import shutil
import face_recognition
import xlwt


date_dir_path='./jixu/2006/061/'
date_dir_path2='./jixu/2006/062/'
result_dir_path='./jixu/2007/result/'
for file in os.listdir(date_dir_path):
    a = date_dir_path + file
    picture_of_01 = face_recognition.load_image_file(a)
    face_encoding_01 = face_recognition.face_encodings(picture_of_01)[0]
    p=1
    t=0
    for file1 in os.listdir(date_dir_path2):
        b = date_dir_path2 + file1
        picture_of_02 = face_recognition.load_image_file(b)
        face_encoding_02 = face_recognition.face_encodings(picture_of_02)[0]
        if len(face_encoding_02) > 0:
         face_encoding_02 = face_recognition.face_encodings(picture_of_02)[0]
         face_distances = face_recognition.face_distance([face_encoding_01], face_encoding_02)
         q=face_distances;
         if q<p:
            p=q
            j=file1
            t=t+1
            print(t)
        else:
            print("No faces found in the image!")
    shutil.copy(a, result_dir_path + file)
    shutil.copy(date_dir_path2+j, result_dir_path + file + "_2.jpg")