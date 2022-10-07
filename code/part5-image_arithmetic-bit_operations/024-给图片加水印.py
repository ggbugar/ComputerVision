# 练习 给图片加水印

import cv2 as cv
import numpy as np

# 暴力方法

# 引入要添加水印得图片
img = cv.imread('../../resources/images/dog.png')

# 显示img
cv.imshow('img', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')

# 创建水印
logo = np.zeros(img.shape, np.uint8)

# 绘制水印
logo[20:60, 20:60] = [0, 0, 255]
logo[40:80, 40:80] = [255, 0, 0]

# 显示logo
cv.imshow('logo', logo)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('logo')

# 计算水印添加的区域，将该区域像素变为全0黑色
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        if logo[i, j][0] > 0:
            img[i, j] = [0, 0, 0]
        elif logo[i, j][1] > 0:
            img[i, j] = [0, 0, 0]
        elif logo[i, j][2] > 0:
            img[i, j] = [0, 0, 0]

# img或上logo
result = cv.bitwise_or(img, logo)

# 显示result
cv.imshow('result', result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('result')

# 其他效果一般的方法
# # 引入图片
# img = cv.imread('../resources/images/dog.png')
# # 创建水印
# watermark = np.zeros(img.shape, np.uint8)
# cv.putText(watermark, "@author lxb", (0, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, 4)
#
# # 直接添加文字
# result = cv.putText(img, "@author lxb", (0, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, 4)
# # 显示运算后的图像
# cv.imshow('result', result)
# if cv.waitKey(0) & 0xFF == ord('q'):
#     cv.destroyWindow('result')
#
# # 使用或运算
# result = cv.bitwise_or(img, watermark)
# # 显示运算后的图像
# cv.imshow('result', result)
# if cv.waitKey(0) & 0xFF == ord('q'):
#     cv.destroyWindow('result')
#
# # 使用图像融合 但会导致图像变暗
# result = cv.addWeighted(img, 0.8, watermark, 0.2, 0)
# # 显示运算后的图像
# cv.imshow('result', result)
# if cv.waitKey(0) & 0xFF == ord('q'):
#     cv.destroyWindow('result')







