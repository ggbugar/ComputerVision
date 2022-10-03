# 高斯滤波
# 作用 解决高斯噪点
# 高斯权重：中间权重高，上下左右权重低，四角更低
# GaussianBlur(img,ksize,sigmaX,sigmaY,borderType=BORDER_DEFAULT)
# 参数说明    img 卷积核大小(n,n) 高斯滤波的延展宽度

import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../resources/images/dog.png')
# 高斯滤波
dst = cv.GaussianBlur(img, (5, 5), sigmaX=100, sigmaY=100)
# 展示卷积前后的图片
cv.imshow('img', img)
cv.imshow('dst', dst)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('dst')

