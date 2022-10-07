# 边缘检测
# 1使用5*5高斯滤波降噪
# 2使用索贝尔从四个方向进行梯度计算（0，45，90，135）
# 3取局部最大值
# 4阈值计算

# Canny(img, minValue, maxValue,...)

import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../../resources/images/dog.png')
# Canny
dst = cv.Canny(img, 150, 200)
# 展示卷积前后的图片
cv.imshow('img', img)
cv.imshow('dst', dst)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('dst')


