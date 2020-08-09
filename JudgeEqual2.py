# -*- coding: utf-8 -*-
from skimage.measure import compare_ssim
import cv2
import os
import time

class CompareImage():

    def compare_image(self, path_image1, path_image2):

        imageA = cv2.imread(path_image1)
        imageB = cv2.imread(path_image2)

        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

        (score, diff) = compare_ssim(grayA, grayB, full=True)
        print("SSIM: {}".format(score))
        return score

start_time=time.time()
compare_image = CompareImage()
rootdir='C:/Users/Administrator/Desktop/test_time/'
images=os.listdir(rootdir)

for base_path in images:
    print(rootdir+base_path)
    for image in images:
        compare_image.compare_image(rootdir+"1.png", rootdir+"2.png")
end_time=time.time()
print(end_time-start_time)