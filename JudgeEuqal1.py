import cv2
import os
import numpy as np
import time
rootdir=''
images=os.listdir(r'C:\Users\Administrator\Desktop\test_time')
start_time=time.time()
for base_name in images:
    for name in images:
        print(base_name)
        image1 = cv2.imread(base_name)

        print(name)
        image2 = cv2.imread(name)
        difference = cv2.subtract(image1,image2)
        result = not np.any(difference) #if difference is all zeros it will return False
        if result==False:
            print(123123123123)
end_time=time.time()
print('totally images',len(images))
print('totally cost',end_time-start_time)

