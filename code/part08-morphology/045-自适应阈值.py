# 自适应阈值
# 为什么需要自适应阈值
# 由于光照不均匀以及阴影的存在，只有一个阈值会使得再阴影处的白色被二值化成黑色
# API
# adaptiveThreshold(img,maxVal,adaptiveMethod,type, blockSize,C)
# adaptiveMethod 计算阈值的方法
#   ADAPTIVE_THRESH_MEAN_C 计算邻近区域的平均值
#   ADAPTIVE_THRESH_GAUSSIAN_C 高斯窗口加权平均值
# type THRESH_BINARY
# blockSize 邻近区域的大小,必须是奇数
# C 常量，应该从计算出的平均值或加权平均值中减去


import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../../resources/images/math.png')
# 转成灰度图
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# maxValue
maxValue = 128
# threshold
dst = cv.adaptiveThreshold(grey, maxValue, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 99, 0)
# 原图
cv.imshow('img', img)
# 灰度图
cv.imshow('grey', grey)
# 二进制化图
cv.imshow('dst', dst)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')
















