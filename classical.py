#!/usr/bin/python
 # -*- coding: UTF-8 -*-

import os
import shutil

src_dir_path = './date'        # 源文件夹
to_dir_path='./face-1/'
to_dir_path2='./face-2/'
key = '_01'                # 源文件夹中的文件包含字符key则复制到to_dir_path文件夹中
if not os.path.exists(to_dir_path):
 print("to_dir_path not exist,so create the dir")
 os.mkdir(to_dir_path,1)
if os.path.exists(src_dir_path):
 print("src_dir_path exitst")
 for file in os.listdir(src_dir_path):
        # is file
        if os.path.isfile(src_dir_path+'/'+file):
            if key in file:
                print('找到包含"'+key+'"字符的文件,绝对路径为----->'+src_dir_path+'/'+file)
                print('复制到----->'+to_dir_path+file)
                shutil.copy(src_dir_path+'/'+file,to_dir_path+'/'+file)
key = '_02'                # 源文件夹中的文件包含字符key则复制到to_dir_path文件夹中
if not os.path.exists(to_dir_path2):
 print("to_dir_path not exist,so create the dir")
 os.mkdir(to_dir_path2,1)
if os.path.exists(src_dir_path):
 print("src_dir_path exitst")
 for file in os.listdir(src_dir_path):
        # is file
        if os.path.isfile(src_dir_path+'/'+file):
            if key in file:
                print('找到包含"'+key+'"字符的文件,绝对路径为----->'+src_dir_path+'/'+file)
                print('复制到----->'+to_dir_path+file)
                shutil.copy(src_dir_path+'/'+file,to_dir_path2+'/'+file)
