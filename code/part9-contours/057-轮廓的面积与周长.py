# 轮廓的面积计算
# API
# contourArea(contour)
# contour 轮廓
#
# 轮廓的周长计算
# API
# arcLength(curve, closed)
# curve 轮廓
# closed 传入轮廓是闭合还是非闭合

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
# 轮廓面积
area = cv.contourArea(contours[2])
print("area=%d" % area)
# 轮廓周长
perimeter = cv.arcLength(contours[2], True)
print("perimeter=%d" % perimeter)
# 画第三个轮廓
contour2 = np.zeros(img.shape, np.uint8)
cv.drawContours(contour2, contours[2], -1, (0, 0, 255), 1)
# 原图
cv.imshow('img', img)
# 灰度图
cv.imshow('grey', grey)
# 二进制化图
cv.imshow('binary', binary)
# 轮廓图
cv.imshow('result', result)
# 显示第三个轮廓
cv.imshow('contour2', contour2)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')





