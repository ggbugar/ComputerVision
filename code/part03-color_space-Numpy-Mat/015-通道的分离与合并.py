# 通道的分离与合并
# API
# split(mat)
# merge((ch1,ch2,...))

import cv2 as cv
import numpy as np
# 读取图像
img = np.zeros((480, 640, 3), np.uint8)
# 通道分离
b, g, r = cv.split(img)
b[10:100, 10:100] = 255
g[10:100, 10:100] = 255
# 通道合并
merge = cv.merge((b, g, r))
# 显示图像
cv.imshow('img', img)
cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('merge', merge)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
