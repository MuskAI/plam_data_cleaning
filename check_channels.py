
import  os
import re
import os.path
import time
import cv2
import numpy as np
start_time=time.time()

def cv_imread(file_path, type=0):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    if (type == 0):
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    return cv_img


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
    for index2,temp_image_name in enumerate(os.listdir(temp_parent)):
        print(temp_image_name,' :(',index2,'/',len(os.listdir(temp_parent)),')')
        full_name=os.path.join(temp_parent,temp_image_name) #这是完整的图片路径
        full_name=full_name.replace('\\','\\\\')
        image=cv2.imread(full_name)
        print(image.size)