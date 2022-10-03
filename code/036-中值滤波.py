# 中值滤波
# 作用 处理胡椒噪音效果极好
# 什么是胡椒噪音，就是一群像胡椒面一样洒在图像上的小点
#
# medianBlur(img, ksize)
# 参数说明    img 卷积核大小int

import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../resources/images/pepperNoise.png')
# 高斯滤波
dst = cv.medianBlur(img, 5)
# 展示卷积前后的图片
cv.imshow('img', img)
cv.imshow('dst', dst)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('dst')
