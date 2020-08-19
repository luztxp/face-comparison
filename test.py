# part1
# 识别图片中的人是谁
import face_recognition
known_image = face_recognition.load_image_file("./face-1/001_01.jpg")
unknown_image = face_recognition.load_image_file("./face-2/001_02.jpg")

lyf_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([lyf_encoding], unknown_encoding)
# A list of True/False values indicating which known_face_encodings match the face encoding to check

print(type(results))
print(results)

if results[0] == True:
  print("yes")
else:
  print("no")
