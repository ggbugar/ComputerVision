# numpy 基本操作
import numpy as np
import cv2 as cv

# 创建矩阵
# 创建数组 array
# 一维数组
arr = np.array([1, 2, 3])
# print(arr)
# 二维数组
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
# print(arr2)
# 创建全0全1数组 zeros/ones
# zeros = np.zeros((480, 640, 3), np.uint8)
# ones = np.ones((480, 640, 3), np.uint8)
# (480, 640, 3) 行 列 通道数
# np.uint8 矩阵中的数据类型
zeros = np.zeros((480, 640, 3), np.uint8)
# print(zeros)
ones = np.ones((480, 640, 3), np.uint8)
# print(ones)
# 创建全值数组 full
# full = np.full((480, 640, 3), initNumber, np.uint8)
# (480, 640, 3) 行 列 通道数
# initNumber 初始值
# np.uint8 矩阵中的数据类型
full = np.full((480, 640, 3), 8, np.uint8)
# print(full)
# 创建单位矩阵 identity/eye
identity = np.identity(4)
# print(identity)
e = np.eye(3, 4)
# print(e)
e = np.eye(3, 4, k=1)
# print(e)
e = np.eye(4, 3, k=1)
# print(e)

# 检索与赋值
# [y,x] [行，列] [y,x,channel]s
arr = np.zeros((4, 4), np.uint8)
arr[0][0]=1
# print(arr)
# print(arr[0])
# print(arr[0][0])

# 图片像素处理 注意opencv为BGR
img = np.zeros((480, 640, 3), np.uint8)
# 整张图片变蓝色
for i in range(0, 480):
    for j in range(0, 640):
        img[i, j, 0] = 255
# 画对角线为绿色
for i in range(0, 480):
    img[i, int(i * 4 / 3)] = [0, 255, 0]
    # img[i, int(i * 4 / 3), 0] = 0
    # img[i, int(i*4/3), 1] = 255
    # img[i, int(i*4/3), 0] = 0
cv.imshow('image', img)
key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyWindow('image')

# 获取子矩阵ROI
# [y1:y2,x1:x2]
# [:,:]或[:]对整个图像进行变更

# 取子矩阵roi
roi = img[100:400, 100:500]
# 对子矩阵赋值
roi[:, :] = [0, 0, 255]
roi[100:250, 100:300] = [0, 255, 0]
# 显示
cv.imshow('image', roi)
key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    cv.destroyWindow('image')

