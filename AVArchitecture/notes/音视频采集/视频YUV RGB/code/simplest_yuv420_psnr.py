import cv2
from numpy import *

def simplest_yuv420_psnr(filepath1, filepath2, width, height, num):
    for i in range(num):
        pic1 = splity_from_yuv420(filepath1, width, height)
        pic2 = splity_from_yuv420(filepath2, width, height)
        mse_sum, mse, psnr = 0, 0, 0
        for j in range(width*height):
            mse_sum += (pic1[j]-pic2[j])**2
        mse = mse_sum/(width*height)
        psnr = 10*log10(255.0*255.0/mse)
        print("PSNR: ", psnr)


def splity_from_yuv420(filepath, width, height):
    fp = open(filepath, 'rb')
    byteArray = []
    for data in fp.read():
        byteArray.append(data)
    e = height * width
    Y = byteArray[0:e]
    # Y = reshape(Y, (height, width))
    return Y

if __name__ == '__main__':
    simplest_yuv420_psnr("../resources/lena_256x256_yuv420p.yuv", "../resources/lena_distort_256x256_yuv420p.yuv", 256, 256, 1)