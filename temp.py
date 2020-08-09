# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import hashlib
import  os
import re
import os.path
import time
from tomd5 import *
start_time=time.time()
def PureImagePath(list):
    New_List=[]
    for parent in list:
        if len(re.findall(r'\\',parent)) ==4:
            New_List.append(parent)
    return New_List
def PureParentPath(list):
    New_List=[]
    for parent in list:
        if len(re.findall(r'\\',parent)) > 2:
            New_List.append(parent)
    return New_List


rootdir = r'E:\Palam_Data'  # 指明被遍历的文件夹

# 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
FileList = []
ParentList=[]
OutputPathName=[]
OutputCode=[]
for parent, dirnames, filenames in os.walk(rootdir):
    # for filename in filenames:
        # FileList.append(os.path.join(parent,filename))
    ParentList.append(parent)
# New_FileList=PureImagePath(FileList)
ParentList=PureParentPath(ParentList)


for index,temp_parent in enumerate(ParentList):
    print("Now we are in ", temp_parent,"(",index,'/',len(ParentList),'):')
    if index ==25:
        break
    for index2,temp_image_name in enumerate(os.listdir(temp_parent)):
        print(temp_image_name,' :(',index2,'/',len(os.listdir(temp_parent)),')')
        full_name=os.path.join(temp_parent,temp_image_name) #这是完整的图片路径
        full_name=full_name.replace('\\','\\\\')
        Md5Code=ImageToMd5(full_name)
        print(Md5Code)
        OutputPathName.append(full_name)
        OutputCode.append(Md5Code)

import csv
print("开始output")
f = open('Image_Md5_Code_ALL_1.csv','w',encoding='utf-8',newline='' )
csv_writer=csv.writer(f)
csv_writer.writerow(['Name','MD5Code'])
for (name,code) in zip(OutputPathName,OutputCode):
    csv_writer.writerow([name,code])
f.close()
end_time=time.time()

print("total time is :",end_time-start_time)