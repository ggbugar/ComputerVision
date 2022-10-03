# 仿射变换 就是图像旋转缩放平移总称
# API:
# warpAffine(src,M,dsize,flags,mode,value)
# 图像，变换矩阵，输出尺寸，
# flags与resize中的插值算法一致使用默认即可，mode外界外推法标志使用默默人即可，填充边界的值使用默认即可）

# 平移矩阵
import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../resources/images/dog.png')
# 获取图片大小
h, w, ch = img.shape
# 设置x和y平移量
x, y = (100, 50)
# 定义平移矩阵
M = np.float32([[1, 0, x], [0, 1, y]])
# 调用API进行平移
translation = cv.warpAffine(img, M, (w, h))
# 展示原图与平移后的对比
cv.imshow('img', img)
cv.imshow('translation', translation)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('translation')








