# 图像卷积
# API
# filter2D(src,ddepth,kernel,anchor,delta,borderType)
# img,位深（设置为-1），卷积核，锚点（默认-1可不设），delta（默认0可不设），边界类型）
# 主要管前面三个参数

import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../resources/images/dog.png')
# 定义5*5的卷积核
kernel = np.ones((5, 5), np.float32)/25
# 图像滤波
dst = cv.filter2D(img, -1, kernel)
# 展示卷积前后的图片
cv.imshow('img', img)
cv.imshow('dst', dst)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('dst')

