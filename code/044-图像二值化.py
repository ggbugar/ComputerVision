# 图像二值化
# 图像二值化 值将图像的每个像素变成两种值 如0和255
# 全局二值化
# 局部二值化

# 全局二值化API
# threshold(img,thresh,maxValue,type)
# 图像（最好是灰度图），阈值，超过阈值替换为maxValue,高于阈值变最大值  cv.THRESH_BINARY


import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../resources/images/dog.png')
# 转成灰度图
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# maxValue
maxValue = 128
# threshold
ret, dst1 = cv.threshold(grey, maxValue, 255, cv.THRESH_BINARY)
ret, dst2 = cv.threshold(grey, maxValue, 255, cv.THRESH_BINARY_INV)
ret, dst3 = cv.threshold(grey, maxValue, 255, cv.THRESH_TRUNC)
ret, dst4 = cv.threshold(grey, maxValue, 255, cv.THRESH_TOZERO)
ret, dst5 = cv.threshold(grey, maxValue, 255, cv.THRESH_TOZERO_INV)
# 原图
cv.imshow('img', img)
# 灰度图
cv.imshow('grey', grey)
# 二进制化图
cv.imshow('dst1', dst1)
cv.imshow('dst2', dst2)
cv.imshow('dst3', dst3)
cv.imshow('dst4', dst4)
cv.imshow('dst5', dst5)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')




