# 绘制文本
# putText(img, 字符串, 起始点, 字体, 字号, 颜色,字粗, 字的线条的型)
# 字体 cv.FONT_... = 0,1,2,3,4,5,6,7,16
# 字号

import cv2 as cv
import numpy as np

# 绘制文本
img = cv.imread('../resources/images/image.png')
# 绘制文本
cv.putText(img, "computer vision", (400, 400), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, 16)
# 显示
cv.imshow('text', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('text')
