# 图像基本变换

# 图像缩放
# resize(src,dst,dsize,fx,fy,interpolation)
# 参数说明:
# 图像地址，目标图像地址（python可不填，为返回值）
# 目标尺寸(x,y)，x轴的缩放因子(与目标尺寸二选一)，y，
# 缩放算法:INIER_NEAREST.INIER_LINEAR,INIER_CUBIC ，INIER_AREA 效果依次序递增，速度依次序递减

import cv2 as cv
import numpy as np

img = cv.imread('../../resources/images/dog.png')
cv.imshow('img', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')

# 按固定尺寸缩放
zoom = cv.resize(img, (640, 480))
cv.imshow('zoom', zoom)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('zoom')

# 按比例缩放
zoom = cv.resize(img, None, fx=0.5, fy=0.5)
cv.imshow('zoom', zoom)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('zoom')

# 放大时使用插值算法
zoom = cv.resize(img, None, fx=1.5, fy=1.5, interpolation=cv.INTER_AREA)
cv.imshow('zoom', zoom)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('zoom')

















