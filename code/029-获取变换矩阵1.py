# 获取变换矩阵
# API
# getRotationMatrix2D(center,angle,scale)
# 中心点，旋转角度（逆时针），缩放比例

# 实例 将图片沿着图片中心逆时针旋转45度
import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../resources/images/dog.png')
# 获取图片大小
h, w, ch = img.shape
# 获取变换矩阵
M = cv.getRotationMatrix2D((w/2, h/2), 45, 1.5)
# 调用API
transform = cv.warpAffine(img, M, (w, h))
# 展示原图与变换后的对比
cv.imshow('img', img)
cv.imshow('transform', transform)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('transform')






