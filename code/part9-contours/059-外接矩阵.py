# 外接矩阵
# 最小外接矩阵
# API
# minAreaRect(points)
# points 坐标点，放轮廓即可
# 返回值 RotatedRect 含角度的矩阵
# RotatedRect 含角度的矩阵，包含以下内容
# x,y起始点
# width,height 长宽
# angle 角度

# 最大外接矩阵
# API
# boundingRect(points)
# points 坐标点，放轮廓即可
# 返回值 Rect 含角度的矩阵
# RotatedRect 含角度的矩阵，包含以下内容
# x,y起始点
# width,height 长宽

import cv2 as cv
import numpy as np

# 读图
img = cv.imread('../../resources/images/externalM.png')
# 转成灰度图
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 二值化
ret, binary = cv.threshold(grey, 128, 255, cv.THRESH_BINARY)
# 查找轮廓
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# 最小外接矩阵
minRect = cv.minAreaRect(contours[1])
# 画最小外接矩阵
box = cv.boxPoints(minRect)
box = np.int0(box)
cv.drawContours(img, [box], 0, (0, 0, 255), 1)
# 最大外接矩阵
x, y, w, h = cv.boundingRect(contours[1])
# 画最大外接矩阵
cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 1)
# 显示外接矩阵
cv.imshow('img', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')















