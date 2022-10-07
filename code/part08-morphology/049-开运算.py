# 开运算=腐蚀（先）+膨胀（后）
# 开运算 可以取去除黑色里面的小白点
# API
# morphologyEx(img, MORPH_OPEN, kernel)
# img,开运算的宏，卷积核（要消除的噪点越大就选越大的卷积核）

import cv2 as cv
import numpy as np
# 导入图片
img = np.zeros((480, 640, 3), np.uint8)
cv.putText(img, "H", (240, 320), cv.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 16, 4)
# 制造噪点
for i in range(0, 10):
    cv.putText(img, ".", (64*i, 48*i), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 4, 4)
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






