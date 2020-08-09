# coding: utf-8
"""统计相同图片的代码，先对比文件大小，然后判断是否长宽相等，最后进行矩阵相减
Created by CHR
2019-11-14

"""
import cv2
import os
import time
import numpy as np
import tomd5
start_time=time.time()

# 可以读取带中文路径的图
def cv_imread(file_path,type=0):
    cv_img=cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    if(type==0):
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    return cv_img


rootdir=r'C:/Users/Administrator/Desktop/test_time/'
images=os.listdir(rootdir)



# 第一步判断文件大小是否相等
# 第二步判断尺寸是否相等
# 第三步逐像素遍历判断，如果相等，则两张图相等
flag1=0
flag2=0
count_time=0
count1=0
count2=0
count3=0
for index1,base_image in enumerate(images):
    count_time = count_time + 1
    print(count_time, "/", len(images))
    for index2,image in enumerate(images):
        if index1==index2:
            continue
        # print(base_image)
        # print(image)
        # print(os.path.getsize(rootdir+base_image))
        # print(os.path.getsize(rootdir+image))
        # print()
        if os.path.getsize(rootdir+base_image)!=os.path.getsize(rootdir+image):
            count1=count1+1
            # print("第一关没有过")
            continue
        else:
            print("到达了第二关")
            img1=cv_imread(rootdir+base_image)
            img2=cv_imread(rootdir+image)
            print(img1.shape)
            if list(img1.shape)[0] != list(img2.shape)[0] or list(img1.shape)[1] != list(img2.shape)[1]:
                count2=count2+1
                print("尺寸不相等")
                continue
            else:
                """
                height, width= img1.shape
                flag_equal=1 #假设相等
                print("进入了最艰难的时刻")
                
                for line in range(height):
                    for pixel in range(width):
                        if img1[line][pixel] != img2[line][pixel]:
                            flag_equal=0 #判断不等
                            break
                        else:
                            continue
                        break
                if flag_equal==1:
                    print("equal")
                    """
                print("开始执行最后一步")
                difference = cv2.subtract(img1, img2)
                result = not np.any(difference)  # if difference is all zeros it will return False
                if result==True:
                    count3=count3+1
                    print("Two Images are equal")
end_time=time.time()
print(count3)
print('the total time is ',end_time-start_time)