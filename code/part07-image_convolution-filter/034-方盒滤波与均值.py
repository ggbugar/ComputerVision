# 方盒滤波
# boxFilter(src,ddepth,ksize,anchor,normalize,borderType)
# 参数说明    img 位深 卷积核大小 锚点-1 True 边界类型

# 均值滤波 常用
# blur(src,ksize,anchor,borderType)
# 主要写前两个参数

import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../../resources/images/dog.png')
# 均值滤波
dst = cv.blur(img, (5, 5))
# 展示卷积前后的图片
cv.imshow('img', img)
cv.imshow('dst', dst)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('dst')

