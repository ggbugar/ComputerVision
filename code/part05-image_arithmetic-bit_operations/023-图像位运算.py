# 图像位运算
# 与     bitwise_not(img)
# 或     bitwise_not(img)
# 非     bitwise_not(img)
# 异或    bitwise_not(img)

import cv2 as cv
import numpy as np

# 画一张图像
img = np.zeros((200, 200, 3), np.uint8)
# 将中间一块变为红色
img[50:150, 50:150] = [0, 0, 255]
# 显示原图像
cv.imshow('img', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')

# img2
img2 = np.zeros((200, 200, 3), np.uint8)
# 全1
img2[:] = [255, 255, 255]
# 执行与运算
result = cv.bitwise_and(img, img2)
# 显示运算后的图像 与1不变，图像为自己
cv.imshow('result', result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('result')

# 执行或运算
result = cv.bitwise_or(img, img2)
# 显示运算后的图像 或1得1，图像为全白
cv.imshow('result', result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('result')

# 执行非运算
result = cv.bitwise_not(img)
# 显示运算后的图像 蓝加绿为青色 图像中间为青色
cv.imshow('result', result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('result')

# 执行异或运算
result = cv.bitwise_xor(img, img)
# 显示运算后的图像 异或自己得0，图像中间为全黑
cv.imshow('result', result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('result')




