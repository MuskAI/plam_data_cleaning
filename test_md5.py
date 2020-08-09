import hashlib
from PIL import Image
import numpy as np


fd = np.array(Image.open(r"C:\\Users\\Administrator\\Desktop\\test_time\\ML_1_1_6.jpg"))
fmd5 = hashlib.md5(fd)
print(fmd5.hexdigest())

