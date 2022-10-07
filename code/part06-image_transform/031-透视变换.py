# 透视变换 将一种坐标系变换为另外一种坐标系
# 用途 可以矫正图像的，将歪的弄成正的
# API
# warpPerspective(img,M,dsize,....)
# 参数与仿射变换参数一致
# getPerspectiveTransform(src,dst)
# 参数与getAffineTransform一致，但需要四个坐标点，四个角

# crook.png
# corrected.png

import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../../resources/images/crook.png')
# 原图点集
src = np.float32([[50, 50], [380, 60], [400, 550], [48, 530]])
# 目标土对应点集
dst = np.float32([[0, 0], [720, 0], [720, 1080], [0, 1080]])
# 获取变换矩阵
M = cv.getPerspectiveTransform(src, dst)
# 变换
corrected = cv.warpPerspective(img, M, (720, 1080))
# 展示变换前后的图片
cv.imshow('img', img)
cv.imshow('corrected', corrected)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('corrected')
# 自动保存图片
cv.imwrite('../../resources/images/corrected.png', corrected)













