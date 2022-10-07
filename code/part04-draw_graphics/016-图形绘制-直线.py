# 画直线
# line(img,开始点,结束点,颜色,线宽,线型)
# 画矩形
# rectangle(img, (0, 0), (1280, 853), (0, 0, 255), 4, 16)
# 调用line画四条直线
# 画圆
# circle(img, 中心点坐标(x,y), 半径, 颜色bgr, 线宽, 线型)

import cv2 as cv
import numpy as np

# 画直线 注意：坐标点是(x,y),颜色可以用bgr,线宽为像素点，线型主要表示平滑程度()取值为-1，4，8，16
img = cv.imread('../../resources/images/image.png')
# 调用API
cv.line(img, (0, 0), (1280, 853), (0, 0, 255), 4, 16)
# 显示图形
cv.imshow('line', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('line')

# 画矩形
img = cv.imread('../../resources/images/image.png')
# 调用API
cv.rectangle(img, (0, 0), (1280, 853), (0, 0, 255), 4, 16)
# cv.line(img, (0, 0), (1280, 0), (0, 0, 255), 4, 16)
# cv.line(img, (1280, 0), (1280, 853), (0, 0, 255), 4, 16)
# cv.line(img, (1280, 853), (0, 853), (0, 0, 255), 4, 16)
# cv.line(img, (0, 853), (0, 0), (0, 0, 255), 4, 16)
cv.imshow('rectangular', img)
# 显示图形
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('rectangular')

# 画圆
img = cv.imread('../../resources/images/image.png')
# 调用API
cv.circle(img, (100, 100), 100, (0, 0, 255), 4, -1)
# 显示图形
cv.imshow('circle', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('circle')








