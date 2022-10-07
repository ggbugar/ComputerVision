# 闭运算=膨胀（先）+腐蚀（后）
# 闭运算 可以取去除白色里面的小黑点
# API
# morphologyEx(img, MORPH_CLOSE, kernel)
# img,闭运算的宏，卷积核（要消除的噪点越大就选越大的卷积核）

import cv2 as cv
import numpy as np
# 导入图片
img = np.zeros((480, 640, 3), np.uint8)
# 制造中心白色区域
img[120:360, 160:480] = [255, 255, 255]
# 制造噪点
for i in range(0, 10):
    cv.putText(img, ".", (64*i, 48*i), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4, 4)
# kernel
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
# morphologyEx
morphologyEx = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
# 原图
cv.imshow('img', img)
# 腐蚀图
cv.imshow('morphologyEx', morphologyEx)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')


















