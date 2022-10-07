# 画椭圆
# ellipse(img, 中心点坐标(x,y), (半长轴x宽，半短轴y高), 角度, 开始角度, 结束角度,颜色,线宽,线型)
# 画图为顺时针，角度表示开始从0度顺时针旋转多少度，开始角度是在此基础上再旋转的度数
# 线宽为-1时，填充整个线条扫过的面积
import cv2 as cv
import numpy as np

# 画椭圆ellipse
img = cv.imread('../../resources/images/image.png')
# 调用API
cv.ellipse(img, (100, 100), (100, 50), 0, 0, 360, (0, 0, 255), -1, 16)
# 显示图形
cv.imshow('ellipse', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('ellipse')

# 画圆
img = cv.imread('../../resources/images/image.png')
# 长半轴等于短半轴
cv.ellipse(img, (100, 100), (100, 100), 0, 0, 360, (0, 0, 255), 4, 6)
# 显示图形
cv.imshow('circle', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('circle')
