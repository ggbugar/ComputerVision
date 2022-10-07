# 获得卷积核
# API
# getStructuringElement(type,size)
# type MOTPH_RECTC（常用）  MOTPH_ELLIPSE  MOTPH_CROSS  腐蚀效果依次递减
# size (n,n) 3 5

import cv2 as cv
import numpy as np
# 导入图片
img = np.zeros((480, 640, 3), np.uint8)
cv.putText(img, "H", (240, 320), cv.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 16, 4)

# 获得kernel
# kernel = np.ones((7, 7), np.uint8)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
# erode
erode = cv.erode(img, kernel, 10)
# 原图
cv.imshow('img', img)
# 腐蚀图
cv.imshow('erode', erode)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')







