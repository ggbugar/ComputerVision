# 拉普拉斯算子
# 拉普拉斯算子可以同时求两个方向的边缘
# 拉普拉斯算子对噪音敏感，得先手动去噪
# API
# Laplacian(src,ddepth,ksize=1,scale=1,delta=0，borderType=border_defalut)
#           img  位深

import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../../resources/images/shudu.png')
# 拉普拉斯算子
dst = cv.Laplacian(img, cv.CV_64F, 1)
# 展示卷积前后的图片
cv.imshow('img', img)
cv.imshow('dst', dst)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('dst')

