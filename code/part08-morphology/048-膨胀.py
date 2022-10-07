# 膨胀
# 处理二值化的图
# API
# dilate(img,kernel,iterations=1)
# img,卷积核(n,n)n越大膨胀效果越明显,膨胀的次数

import cv2 as cv
import numpy as np
# 导入图片
img = np.zeros((480, 640, 3), np.uint8)
cv.putText(img, "H", (240, 320), cv.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 16, 4)

# 获得kernel
# kernel = np.ones((7, 7), np.uint8)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (7, 7))
# dilate
dilate = cv.dilate(img, kernel, 10)
# 原图
cv.imshow('img', img)
# 膨胀图
cv.imshow('erode', dilate)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')
