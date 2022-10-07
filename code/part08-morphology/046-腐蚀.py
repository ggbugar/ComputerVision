# 腐蚀
# 腐蚀卷积核通常为全1
# API
# erode(img,kernel,iterations=1)
# img,卷积核(n,n)n越大腐蚀效果越明显,腐蚀的次数

import cv2 as cv
import numpy as np
# 导入图片
img = np.zeros((480, 640, 3), np.uint8)
cv.putText(img, "H", (240, 320), cv.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 16, 4)

# kernel
kernel = np.ones((7, 7), np.uint8)
# erode
erode = cv.erode(img, kernel, 10)
# 原图
cv.imshow('img', img)
# 腐蚀图
cv.imshow('erode', erode)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')












