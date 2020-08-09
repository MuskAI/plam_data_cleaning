import re
name='179-女-27-左[1]'
name1='179-男女-27-左[1]'
name2='E:\\Palam_Data\\9心脑血管疾病\\7早期心脏病\\999-男-35-右[2].jpg'
result=re.findall('(\\\\)',name2)
class_search = re.search(r'(\w:\\\w*\\)(\d*)(\w+\\)(\d*)(\w*\\)(.*)(\.\w*)', name2)

# 大类标签和小类标签分别为2和4 6是图片名称
temp=class_search.group()
# temp=temp_name.replace('.jpg','')
temp=temp.replace('\\','\\\\')
# print(temp)
len1=['asd','sdfsdf']

#print(len(len1 ))
list='E:\\Palam_Data\\.idea'
# print(len(re.findall(r'\\',list)))
class_search = re.search(r'(\w:\\\w*\\)(\d*)(\w+\\)(\d*)(\w*\\)(.*)(\.\w*)', name2)
# print(class_search.group())

name3=['E:\\Palam_Data\\9心脑血管疾病\\7早期心脏病\\999-男-35-右[2].jpg','E:\\Palam_Data\\9心脑血管疾病\\7早期心脏病\\999-男-35-右[2].jpg']
import pandas as pd
import csv
f = open('Error_path1.csv','w',encoding='utf-8',newline='' )
csv_writer=csv.writer(f)
csv_writer.writerow(['Name'])

for datas in name3:
    csv_writer.writerow(datas.split('~'))
f.close()