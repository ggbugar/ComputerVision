# 黑帽运算
# 黑帽=原图-闭运算 得白区域中的小黑噪点
# 表现为白点，用原图与运算即可抠出原图的噪点
# API
# morphologyEx(img, MORPH_BLACKHAT, kernel)
# img,黑帽运算的宏，卷积核（越大越好）

import cv2 as cv
import numpy as np
# 导入图片
img = np.zeros((480, 640, 3), np.uint8)
# 制造中心白块
img[120:360, 160:480] = [255, 255, 255]
# 制造噪点
for i in range(0, 10):
    cv.putText(img, ".", (64*i, 48*i), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4, 4)
# kernel
kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
# morphologyEx
morphologyEx = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
# 原图
cv.imshow('img', img)
# 黑帽图
cv.imshow('morphologyEx', morphologyEx)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')
