import cv2 as cv
import numpy as np


# 定义回调函数
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)


# 创建窗口
cv.namedWindow('mouse')
cv.resizeWindow('mouse', 640, 360)

# 给窗口设置鼠标回调函数
cv.setMouseCallback('mouse', mouse_callback, '123')

# 创建一张黑图片
img = cv.imread('../../resources/images/image.png')
while True:
    # 显示窗口
    cv.imshow('mouse', img)
    key = cv.waitKey(10)
    if key & 0xFF == ord('q'):
        break
# 关闭窗口
cv.destroyWindow('mouse')
