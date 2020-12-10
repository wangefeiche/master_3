import cv2 as cv2  # OpenCV import
import numpy as np


def YUVtoRGB(filepath, height, width):
    fp = open(filepath, 'rb')
    byteArray = []
    for data in fp.read():
        byteArray.append(data)
    e = height * width
    Y = byteArray[0:e]
    Y = np.reshape(Y, (height, width))

    s = e
    V = byteArray[s:s+s//4]
    V = np.repeat(V, 2, 0)
    V = np.reshape(V, (width//2, height))
    V = np.repeat(V, 2, 0)

    U = byteArray[s+s//4:]
    U = np.repeat(U, 2, 0)
    U = np.reshape(U, (width//2, height))
    U = np.repeat(U, 2, 0)

    RGBMatrix = (np.dstack([Y, U, V])).astype(np.uint8)
    RGBMatrix = cv2.cvtColor(RGBMatrix, cv2.COLOR_YUV2RGB, 3)
    return RGBMatrix

if __name__ == '__main__':
    img = YUVtoRGB('../resources/lena_256x256_yuv420p.yuv', 256, 256)
    cv2.imshow("sohow", img)
    cv2.waitKey(0)