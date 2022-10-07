# createTrackbar
# createTrackbar参数
#     trackbarName
#     winname
#     value trackbar当前值
#     count 最小值0，最大值为count，最大255
#     callback
#     userdata
# getTrackbarPos
# getTrackbarPos参数
#     trackbarName
#     winname

# 实战
# 通过trackbar调整图片颜色
import cv2 as cv
import numpy as np


# 定义一个回调函数
def callback():
    pass


# 创建窗口
cv.namedWindow('trackbar')
cv.resizeWindow('trackbar', 640, 480)
# 创建trackbar
cv.createTrackbar('R', 'trackbar', 0, 255, callback)
cv.createTrackbar('G', 'trackbar', 0, 255, callback)
cv.createTrackbar('B', 'trackbar', 0, 255, callback)
# 创建一个背景图片
img = np.zeros((480, 640, 3), np.uint8)
while True:
    # 获取当前trackbar的值
    r = cv.getTrackbarPos('R', 'trackbar')
    g = cv.getTrackbarPos('G', 'trackbar')
    b = cv.getTrackbarPos('B', 'trackbar')
    # 改变图片颜色
    img[:] = [b, g, r]
    # 显示图片
    cv.imshow('trackbar', img)
    key = cv.waitKey(10)
    if key & 0xFF == ord('q'):
        break
# 关闭窗口
cv.destroyWindow('trackbar')
