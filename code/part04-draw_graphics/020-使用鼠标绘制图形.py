# 基本功能
# 通过鼠标进行基本图形的绘制
# 可以画线，按l键选择画线，滑动鼠标即可画线
# 可以画矩形，按r键选择画矩形，滑动鼠标即可画矩形
# 可以画圆，按c键选择画圆，滑动鼠标即可画圆
# ...

import cv2 as cv
import numpy as np

# 全局变量 当前该画的形状
currentShape = 0
# 全局变量 鼠标按下位置
startpos = (0, 0)

# 创建窗口
cv.namedWindow('drawShape')
cv.resizeWindow('drawShape', 640, 480)
# 读取图片
img = cv.imread('../../resources/images/image.png')


# 鼠标回调函数
def callback(event, x, y, flags, userdata):
    global currentShape, startpos
    # 左键按下
    if event & cv.EVENT_LBUTTONDOWN == cv.EVENT_LBUTTONDOWN:
        startpos = (x, y)
    elif event & cv.EVENT_LBUTTONUP == cv.EVENT_LBUTTONUP:
        if currentShape == 0:
            cv.line(img, startpos, (x, y), (0, 0, 255))
        elif currentShape == 1:
            cv.rectangle(img, startpos, (x, y), (0, 0, 255))
        elif currentShape == 2:
            a = x - startpos[0]
            b = y - startpos[1]
            r = int((a ** 2 + b ** 2) ** 0.5)
            cv.circle(img, startpos, r, (0, 0, 255))
        else:
            print('error:no shape')


# 给窗口设置鼠标回调函数
cv.setMouseCallback('drawShape', callback)

while True:
    cv.imshow('drawShape', img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        # quit
        cv.destroyWindow('drawShape')
        break
    elif key == ord('l'):
        # line
        currentShape = 0
    elif key == ord('r'):
        # rectangle
        currentShape = 1
    elif key == ord('c'):
        # circle
        currentShape = 2
