# 图像的加减乘除
# 对应位置的元素相互加减乘除，而不是矩阵乘法和逆

import cv2 as cv
import numpy as np

# 读取图片
dog = cv.imread('../../resources/images/dog.png')

# 获取dog的属性
# print(dog.shape)

# 要运算的图片
img = np.ones(dog.shape, np.uint8) * 50
# img = np.ones((720, 1080, 3), np.uint8) * 50

# 显示原图
cv.imshow('dog', dog)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('dog')

# 加法add
# 使图像更加光亮
add = cv.add(dog, img)
cv.imshow('add', add)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('add')

# 减法subtract
# 使图像更暗
subtract = cv.subtract(dog, img)
cv.imshow('subtract', subtract)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('subtract')

img = np.ones(dog.shape, np.uint8) * 2

# 乘法
multiply = cv.multiply(dog, img)
cv.imshow('multiply', multiply)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('multiply')

# 除法
divide = cv.divide(dog, img)
cv.imshow('divide', divide)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('divide')













