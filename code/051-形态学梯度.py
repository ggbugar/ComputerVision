# 形态学梯度
# 梯度=原图-腐蚀 得边缘
# API
# morphologyEx(img, MORPH_GRADIENT, kernel)
# img,梯度运算的宏，卷积核（卷积核越小被腐蚀的越少，边缘越清晰）

import cv2 as cv
import numpy as np
# 导入图片
img = np.zeros((480, 640, 3), np.uint8)
cv.putText(img, "H", (240, 320), cv.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 16, 4)
# kernel
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
# morphologyEx
morphologyEx = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
# 原图
cv.imshow('img', img)
# 腐蚀图
cv.imshow('morphologyEx', morphologyEx)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')


