# 图像分割——分水岭法
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# 获取背景
# 1. 通过二值法得到黑白图片
# 2. 通过形态学获取背景
# 读取图片
img = cv.imread('../resources/images/water_coins.jpeg')
# 转灰度图
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 二值化
ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
# 开运算去除噪点
kernel = np.ones((3, 3), np.int8)
opened = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
# 膨胀得到背景
background = cv.dilate(opened, kernel, iterations=1)
# 获取前景物体
# 距离变换
dist = cv.distanceTransform(opened, cv.DIST_L2, 5)
# 获取前景物体
ret, forward_ground = cv.threshold(dist, 0.7*dist.max(), 255, cv.THRESH_BINARY)
# plt.imshow(dist, cmap='gray')
# plt.show()
# exit()
# 转换
forward_ground = np.uint8(forward_ground)
# 获取未知区域
unknown = cv.subtract(background, forward_ground)
# 创建连通域maker
ret, marker = cv.connectedComponents(forward_ground)
# 设置maker
marker = marker + 1
marker[unknown == 255] = 0
# 进行图像分割
result = cv.watershed(img, marker)
# 结果的边缘用-1表示，将其标红
img[result == -1] = [0, 0, 255]

cv.imshow("img", img)
cv.imshow("unknown", unknown)
cv.imshow("forward_ground", forward_ground)
cv.imshow("background", background)
cv.imshow("thresh", thresh)
cv.waitKey()


























