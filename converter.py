"""Converts png, bmp and gif to jpg, removes descriptions and resizes the image to a maximum of 1920x1080."""

from PIL import Image
from glob import glob
import PIL
import sys
import os
import cv2


path = 'E:\\palam_test\\bianmi_new\\'
path_originals = 'E:\\palam_test\\1便秘\\'

if not os.path.exists(path):
    os.makedirs(path)

def compress_image(image, infile):
    size = 1920, 1080
    width = 1920
    height = 1080
    listing = os.listdir(path_originals)

    name = infile.split('.')
    first_name = path+'/'+name[0] + '.jpg'
    if image.size[0] > width and image.size[1] > height:
        image.thumbnail(size, Image.ANTIALIAS)
        image.save(first_name, quality=100)
    elif image.size[0] > width:
        wpercent = (width/float(image.size[0]))
        height = int((float(image.size[1])*float(wpercent)))
        image = image.resize((width,height), PIL.Image.ANTIALIAS)
        image.save(first_name,quality=100)
    elif image.size[1] > height:
        wpercent = (height/float(image.size[1]))
        width = int((float(image.size[0])*float(wpercent)))
        image = image.resize((width,height), PIL.Image.ANTIALIAS)
        image.save(first_name, quality=100)
    else:
        image.save(first_name, quality=100)


def processImage():
    count_jpeg=0
    count_gif=0
    count_png=0
    count_bmp=0
    count_sum=0
    listing = os.listdir(path_originals)
    for infile in listing:
        print(infile)
        img = Image.open(path_originals+infile)
        name = infile.split('.')
        first_name = path+'/'+name[0] + '.jpg'
        count_sum =count_sum+1
        if img.format == "JPEG":
            image = img.convert('RGB')
            compress_image(image, infile)
            # cv2.imwrite(first_name,image)
            img.close()
            count_jpeg=count_jpeg+1
        elif img.format == "GIF":
            i = img.convert("RGBA")
            bg = Image.new("RGBA", i.size)
            image = Image.composite(i, bg, i)
            compress_image(image, infile)
            # cv2.imwrite(first_name,image)
            img.close()
            count_gif=count_gif+1
        elif img.format == "PNG":
            try:
                image = Image.new("RGB", img.size, (255, 255, 255))
                image.paste(img,img)
                # cv2.imwrite(first_name,image)
                compress_image(image, infile)
            except ValueError:
                image = img.convert('RGB')
                compress_image(image, infile)
                # cv2.imwrite(first_name,image)
            img.close()
            count_png=count_png+1
        elif img.format == "BMP":
            image = img.convert('RGB')
            compress_image(image, infile)
            # cv2.imwrite(first_name,image)
            img.close()
            count_bmp=count_bmp+1

    print("the number of jepg:", count_jpeg)
    print("the number of png:",count_png)
    print("the number of bmp:",count_bmp)
    print("the number of gif",count_gif)

processImage()
