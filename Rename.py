# encoding: utf-8
import os
import os.path
import re
import pandas as pd
Error_name=0
Error_path=[]
def StandardName_SexAndHand(used_name,used_path):
    sex = re.findall('男|女|W|M|w|m', used_name)
    if len(sex) == 1:
        if '男' or 'm' or 'M' in sex:
            new_sex = 'M'
        elif '女' or 'W' or 'w' in sex:
            new_sex = 'W'
        else:
            Error_path.append(used_path)
            print('性别匹配错误！')
    elif len(sex) == 0:
        new_sex = 'U'
        Error_path.append(used_path)
    else:
        new_sex = 'U'
        Error_path.append(used_path)
        """
        print(used_name, '该文件名有误，请手动确定性别:')
        sex_flag = input('1.男  2女 3未知：')
        if sex_flag == '1':
            new_sex = 'M'
        elif sex_flag == '0':
            new_sex = 'W'
        else:
            new_sex = 'U'
        """

    hand = re.findall('左|右|L|R|l|r', used_name)
    if len(hand) == 1:
        if '左' or 'L' or 'l' in hand:
            new_hand = 'L'
        elif '右' or 'R' or 'r' in hand:
            new_hand = 'R'
        else:
            Error_path.append(used_path)
            print('左右手匹配错误！')
    elif len(sex) == 0:
        new_hand = 'U'
        Error_path.append(used_path)
    else:
        new_hand = 'U'
        Error_path.append(used_path)
        """
        print(used_name, '该文件名有误，请手动确定左右手:')
        sex_flag = input('1.左  2.右 3.未知：')
        if sex_flag == '1':
            new_hand = 'L'
        elif sex_flag == '0':
            new_hand = 'R'
        else:
            new_hand = 'UNKOWN'
        """
    return new_sex, new_hand
def StandardName(used_path,num):
    # 大类标签和小类标签分别为2和4
    used_path=used_path.replace('\\\\','\\')
    class_search = re.search(r'(\w:\\\w*\\)(\d*)(\w+\\)(\d*)(\w*\\)(.*)(\.\w*)', used_path)
    # 大类标签和小类标签分别为2和4 6是图片名称 7是图片后缀
    temp_name=class_search.group(6)
    new_sex_temp, new_hand_temp = StandardName_SexAndHand(temp_name,used_path)
    return (new_sex_temp+new_hand_temp+'_'+class_search.group(2)+'_'+class_search.group(4)+'_'+str(num)),str(class_search.group(7))
def ClassNumber(path):
    list_path = re.search(r'(\w:\\\w*\\)(\d*)(\w+\\)(\d*)(\w*)', path)
    list_path =list_path.replace('\\', '/')
    return len(os.listdir(list_path))
def PureParentPath(list):
    New_List=[]
    for parent in list:
        if len(re.findall(r'\\',parent)) > 2:
            New_List.append(parent)
    return New_List
def PureImagePath(list):
    New_List=[]
    for parent in list:
        if len(re.findall(r'\\',parent)) ==4:
            New_List.append(parent)
    return New_List
rootdir = r'E:\Palam_Data'  # 指明被遍历的文件夹
count=0
# 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
FileList = []
ParentList=[]
for parent, dirnames, filenames in os.walk(rootdir):
    # for filename in filenames:
        # FileList.append(os.path.join(parent,filename))
    ParentList.append(parent)
# New_FileList=PureImagePath(FileList)
ParentList=PureParentPath(ParentList)

for index,temp_parent in enumerate(ParentList):
    print("Now we are in ", temp_parent,"(",index,'/',len(ParentList),'):')
    for index2,temp_image_name in enumerate(os.listdir(temp_parent)):
        # print(temp_image_name,' :(',index2,'/',len(os.listdir(temp_parent)),')')
        full_name=os.path.join(temp_parent,temp_image_name) #这是完整的图片路径
        full_name=full_name.replace('\\','\\\\')
        # print(full_name) #打印完整的图片路径
        std_name, image_format=StandardName(full_name,index2+1)# 转换为标准的名称
        std_full_name=os.path.join(temp_parent,std_name+image_format)
        std_full_name=std_full_name.replace('\\','\\\\')
        print('转换前的:', full_name,'\n','转换后的:',std_full_name)
        temp_image_name=temp_image_name.replace('\\','/')

        if full_name!=std_full_name and not os.path.exists(std_full_name):
            os.rename(full_name,std_full_name)


import csv
print("开始output")
f = open('Error_path2.csv','w',encoding='utf-8',newline='' )
csv_writer=csv.writer(f)
csv_writer.writerow(['Name'])
print(Error_path)
print(len(Error_path))
for datas in Error_path:
    csv_writer.writerow(datas.split('~'))
f.close()