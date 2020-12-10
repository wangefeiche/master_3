import cv2
from numpy import *
from bmp_structure import bmp

def simplest_rgb24_to_bmp(filepath, width, height, outpath):
    bmp_img = bmp(width, height)
    bmp_img.gen_bmp_header()
    bmp_img.print_bmp_header()
    fp = open(filepath, 'rb')
    byteArray = []
    for data in fp.read():
        byteArray.append(data)
    RGBMatrix = [], [], []
    for j in range(width * height):
        RGBMatrix
        R.append(byteArray[3 * j])
        G.append(byteArray[3 * j + 1])
        B.append(byteArray[3 * j + 2])
    Rt = reshape(R, (width, height))
    Gt = reshape(G, (width, height))
    Bt = reshape(B, (width, height))


if __name__ == '__main__':
    simplest_rgb24_to_bmp("../resources/cie1931_500x500.rgb", 500, 500, 'save1.bmp')