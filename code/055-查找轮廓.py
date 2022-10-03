import cv2 as cv
import numpy as np

img = cv.imread('../resources/images/outline.png')
# 转成灰度图
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 二值化
ret, binary = cv.threshold(grey, 128, 255, cv.THRESH_BINARY)
# 查找轮廓
contours, hierarchy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# 原图
cv.imshow('img', img)
# 灰度图
cv.imshow('grey', grey)
# 二进制化图
cv.imshow('binary', binary)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')

