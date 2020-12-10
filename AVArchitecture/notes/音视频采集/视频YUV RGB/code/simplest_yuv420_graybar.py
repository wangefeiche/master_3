import cv2
from numpy import *

def simplest_yuv420_graybar(width, height, ymin, ymax, barnum):
    barwidth = width / barnum
    lum_inc = (ymax - ymin) / (barnum-1)
    uv_width = width // 2
    uv_height = height // 2

    data_y = [0]*width*height
    data_u = [0]*uv_width*uv_height
    data_v = [0]*uv_width*uv_height
    print("Y, U, V value from picture's left to right:")
    for t in range(barnum):
        lum_temp = ymin+(t * lum_inc)
        print("128, 128", lum_temp)

    for j in range(height):
        for i in range(width):
            t = i//barwidth
            lum_temp = ymin+(t * lum_inc)
            data_y[j*width+i] = lum_temp
    for j in range(uv_height):
        for i in range(uv_width):
            data_u[j*uv_width+i] = 128
    for j in range(uv_height):
        for i in range(uv_width):
            data_v[j * uv_width + i] = 128

    Yt = reshape(data_y, (width, height))

    Vt = repeat(data_v, 2, 0)
    Vt = reshape(Vt, (width // 2, height))
    Vt = repeat(Vt, 2, 0)

    Ut = repeat(data_u, 2, 0)
    Ut = reshape(Ut, (width // 2, height))
    Ut = repeat(Ut, 2, 0)

    RGBMatrix = (dstack([Yt, Ut, Vt])).astype(uint8)
    RGBMatrix = cv2.cvtColor(RGBMatrix, cv2.COLOR_YUV2RGB, 3)
    cv2.imshow("sohow", RGBMatrix)
    cv2.waitKey(0)

if __name__ == '__main__':
    width = 256
    height = 256
    simplest_yuv420_graybar(width, height, 0, 255, 10)
