# 获得变换矩阵的第二种方法
# getAffineTransform(src[], dst[])
# 传入坐标点集合

# 实例 将图片沿着图片中心顺时针旋转30度
import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../resources/images/dog.png')
# 获取图片大小
h, w, ch = img.shape
# src 和 dst
src = np.float32([[0, 0], [60, 0], [30, 52]])
dst = np.float32([[0, 0], [52, 30], [0, 60]])
# 获取变换矩阵
M = cv.getAffineTransform(src, dst)
# 调用API
transform = cv.warpAffine(img, M, (w, h))
# 展示原图与变换后的对比
cv.imshow('img', img)
cv.imshow('transform', transform)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('transform')




