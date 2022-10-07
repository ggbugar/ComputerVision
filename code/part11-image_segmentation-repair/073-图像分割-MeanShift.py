# cv.pyrMeanShiftFiltering
# (img,
# double sp,半径
# double sr,色彩幅值
# maxLevel=1,
# termcrit=TermCriteria)

import cv2 as cv
import numpy as np
# 读取文件
img = cv.imread('../../resources/images/flower.png')
#
mean_img = cv.pyrMeanShiftFiltering(img, 20, 30)
# canny边缘查找
canny = cv.Canny(mean_img, 150, 300)
# 轮廓查找
contours, _ = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# 画轮廓
cv.drawContours(img, contours, -1, (0, 0, 255), 2)
# 显示各级结果
cv.imshow('mean_img', mean_img)
cv.imshow('canny', canny)
cv.imshow('img', img)
if cv.waitKey() & 0xFF == ord('q'):
    cv.destroyAllWindows()
