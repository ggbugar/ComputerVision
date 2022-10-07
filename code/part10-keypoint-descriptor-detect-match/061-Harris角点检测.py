# 角点
# 光滑地区，无论向哪里移动，衡量系数都不变
# 边缘地区，垂直边缘移动时，衡量系数变化剧烈
# 焦点处，往任何方向移动，衡量系数变化剧烈
# API Harris角点检测
# cornerHarris(img,dst,blockSize,ksize,k)
# img
# 检测窗口大小
# 索贝尔卷积核
# 权重系数经验值0.噢到0.04，取0，04
# 返回值为角点的矩阵dst

import cv2 as cv
import numpy as np
blockSize = 2
ksize = 3
k = 0.04

img = cv.imread('../../resources/images/shudu.png')
# 灰度化
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
dst = cv.cornerHarris(grey, blockSize, ksize, k)
# 角点展示
img[dst > 0.01*dst.max()] = [0, 0, 255]
cv.imshow('harris', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()










