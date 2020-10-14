import cv2
import numpy as np
import sys
import os
import fnmatch


def sharpen(image):
    kernal = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    newimg = cv2.filter2D(image, -1, kernal)
    cv2.imshow('Sharpen',newimg)
    cv2.waitKey(0)
    return newimg

def blur(image):
    kernals =[3, 5, 9, 13]
    for idx, k in enumerate(kernals):
        iamge_bl =cv2.blur(image, ksize= (k, k))
        cv2.imshow(str(k), iamge_bl)
        cv2.waitKey(0)
    return

def resize(fname, width, height):
    image = cv2.imread(fname)
    cv2.imshow('Original Image',image) ##show image
    cv2.waitKey(0)

    org_width, org_height = image.shape[0:2] ##print size and resize image
    print('Width:',org_width)
    print('Height:',org_height)
    if org_width >= org_height:
        new_img = cv2.resize(image,(width, height))
    else:
        new_img =  cv2.resize(image,(height, width))
    return  fname, new_img
listoffile =os.listdir('.')
pattern ="*.JPG"
n =len(sys.argv)

if n == 3:
    width =int(sys.argv[1])
    heigth = int(sys.argv[2])
else:
    width = 600
    heigth = 300
if not os.path.exists('NewFolder'):
    os.makedirs('NewFolder')
for filename in listoffile:
    if fnmatch.fnmatch(filename, pattern):
        filename, new_img = resize(filename, width, heigth)
        cv2.imwrite('NewFolder\\' + filename, new_img)
filename, new_img = resize('forresize.JPG', 600, 400)
cv2.imshow('resized',new_img)
cv2.waitKey(0)
blur(new_img)
image = sharpen(new_img)