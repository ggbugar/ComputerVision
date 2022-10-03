# Scharr(src,ddepth,dx,dy,scale=1,delta=0，borderType=border_defalut)
#      img 位深 对谁求导

import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../resources/images/shudu.png')
# 沙尔算子y方向边缘
d1 = cv.Scharr(img, cv.CV_64F, 1, 0)
# 沙尔算子x方向边缘
d2 = cv.Scharr(img, cv.CV_64F, 0, 1)
# 加法
dst = cv.add(d1, d2)
# 展示卷积前后的图片
cv.imshow('img', img)
cv.imshow('d1', d1)
cv.imshow('d2', d2)
cv.imshow('dst', dst)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('dst')

