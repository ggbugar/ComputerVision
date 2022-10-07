# 绘制轮廓
# API
# drawContours(
# img,
# contours,
# contoursIdx =-1表示绘制所有轮廓,
# color,颜色(0,0,255)
# thickness,线宽，-1辨识全部填充
# ..)

import cv2 as cv
import numpy as np
# 读图
img = cv.imread('../../resources/images/outline.png')
# 转成灰度图
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 二值化
ret, binary = cv.threshold(grey, 128, 255, cv.THRESH_BINARY)
# 查找轮廓
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# 绘制轮廓
result = np.zeros(img.shape, np.uint8)
cv.drawContours(result, contours, -1, (0, 0, 255), 1)

# 原图
cv.imshow('img', img)
# 灰度图
cv.imshow('grey', grey)
# 二进制化图
cv.imshow('binary', binary)
# 轮廓图
cv.imshow('result', result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')

