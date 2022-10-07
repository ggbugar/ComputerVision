# 画多边形
# polylines(img, 点集 [points], 是否闭环True, 颜色bgr,...)
# 点集必须是32位的 np.int32 [points]
# 是否闭环 True
# 填充多边形fillPoly(img,点集，颜色）

import cv2 as cv
import numpy as np

# 画多边形
img = cv.imread('../../resources/images/image.png')
# create points
points = np.array([(0, 0), (200, 100), (200, 200), (0, 100)], np.int32)
# 画多边形
cv.polylines(img, [points], True, (0, 0, 255), 4, 16)
# 填充颜色
cv.fillPoly(img, [points], (0, 255, 0))
# 显示图形
cv.imshow('polylines', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('polylines')
