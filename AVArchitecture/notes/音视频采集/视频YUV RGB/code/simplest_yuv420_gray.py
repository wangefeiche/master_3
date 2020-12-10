import cv2
from numpy import *
from PIL import Image

screenLevels = 255.0


def yuv_import(filename, dims, numfrm, startfrm):
    fp = open(filename, 'rb')
    blk_size = prod(dims) * 3 // 2
    fp.seek(blk_size * startfrm, 0)
    Y = []
    U = []
    V = []
    print(dims[0])
    print(dims[1])
    d00 = dims[0]
    d01 = dims[1]
    print(d00)
    print(d01)
    Yt = zeros((dims[0], dims[1]), uint8, 'C')
    Ut = zeros((d00, d01), uint8, 'C')
    Vt = zeros((d00, d01), uint8, 'C')
    for i in range(numfrm):
        for m in range(dims[0]):
            for n in range(dims[1]):
                # print m,n
                Yt[m, n] = ord(fp.read(1))
        for m in range(d00):
            for n in range(d01):
                Ut[m, n] = 128
        for m in range(d00):
            for n in range(d01):
                Vt[m, n] = 128
    Y = Y + [Yt]
    U = U + [Ut]
    V = V + [Vt]
    fp.close()
    return Y, U, V


if __name__ == '__main__':
    width = 256
    height = 256
    data = yuv_import('../resources/lena_256x256_yuv420p.yuv', (height, width), 1, 0)
    RGBMatrix = (dstack([data[0][0], data[1][0], data[2][0]])).astype(uint8)
    RGBMatrix = cv2.cvtColor(RGBMatrix, cv2.COLOR_YUV2RGB, 3)
    cv2.imshow("sohow", RGBMatrix)
    cv2.waitKey(0)
