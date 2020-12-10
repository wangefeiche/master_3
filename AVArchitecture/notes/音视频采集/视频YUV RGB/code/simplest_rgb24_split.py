import cv2
from numpy import *

def simplest_rgb24_split(filepath, width, height, num):
    for i in range(num):
        fp = open(filepath, 'rb')
        byteArray = []
        for data in fp.read():
            byteArray.append(data)
        R, G, B = [], [], []
        for j in range(width*height):
            R.append(byteArray[3*j])
            G.append(byteArray[3*j+1])
            B.append(byteArray[3*j+2])
        Rt = reshape(R, (width, height))
        Gt = reshape(G, (width, height))
        Bt = reshape(B, (width, height))
        RGBMatrix = (dstack([Rt, Gt, Bt])).astype(uint8)
        cv2.imshow("sohow", RGBMatrix[:,:,2])
        cv2.waitKey(0)

if __name__ == '__main__':
    simplest_rgb24_split("../resources/cie1931_500x500.rgb", 500, 500, 1)