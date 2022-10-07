# 多边形逼近与凸包
# 多边形逼近
# API
# approxPolyDB(curve,epsilon,closed)
# curve 曲线，轮廓
# curve 精度,数值越小精度越高
# closed 是否闭合
#
# 凸包
# API
# convexHull(points,clockwise,...)
# points 点，轮廓
# clockwise 顺时针True,逆时针False
#

# 多边形逼近
import cv2 as cv
import numpy as np


# 自定义画轮廓的函数
def drawOutline(src, points):
    i = 0
    while i < len(points):
        # 如果是最后一个点则连回第一个点
        if i == len(points) - 1:
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv.line(src, (x, y), (x1, y1), (0, 0, 255), 1)
        else:
            x, y = points[i][0]
            x1, y1 = points[i + 1][0]
            cv.line(src, (x, y), (x1, y1), (0, 0, 255), 1)
        i = i + 1


# 读图
img = cv.imread('../../resources/images/hand.png')
# 转成灰度图
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 二值化
ret, binary = cv.threshold(grey, 128, 255, cv.THRESH_BINARY)
# 查找轮廓
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# 设置多边形逼近的精度
curve = 10
# 多边形逼近
approx = cv.approxPolyDP(contours[0], curve, True)
# 凸包
hull = cv.convexHull(contours[0])
# 画多边形逼近的轮廓
drawOutline(img, approx)
# 画凸包的轮廓
drawOutline(img, hull)
# 原图的轮廓图
cv.imshow('img', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')
