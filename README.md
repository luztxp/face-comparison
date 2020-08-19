# face-comparison
昨天老师打电话，叫我写个程序对学籍照片和毕业照片进行比对，筛选可能顶替上大学的学生.选择用face_recognition。

首先需要安装cmake 

pip install cmake

安装dlib，指定版本19.7.0

pip install dlib==19.7.0

最后安装face_recognition

pip install face_recognition

若是所有图片都在一个文件夹用classical进行分类，用rename重命名照片，根据xlsx重命名，运行facecomparion.py输出人脸比对的face distence到xlsx。
