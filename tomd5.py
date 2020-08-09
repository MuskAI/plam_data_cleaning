import hashlib
from PIL import Image
import numpy as np

"""
这是一个将图片进行md5编码并返回一个字符串
"""

def ImageToMd5(image_path):
    fd = np.array(Image.open(image_path))
    fmd5 = hashlib.md5(fd)
    return fmd5.hexdigest()
