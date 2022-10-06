# harris角点检测具有旋转不变的缺陷
# SIFT解决该缺陷
# 使用步骤：
#   创建SIFT对象 sift = cv.xfeatures2d.SIFT_create()
#   进行检测，kp=sift.detect(img,...)
#   绘制关键点cv.drawKeypoints(grey,kp,img)

import cv2 as cv
import numpy as np

img = cv.imread('../resources/images/shudu.png')
# 灰度化
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 创建SIFT对象
sift = cv.xfeatures2d.SIFT_create()
# 进行检测，kp=sift.detect(img,...)
kp = sift.detect(gray, None)
# 绘制关键点cv.drawKeypoint(grey,kp,img)
cv.drawKeypoints(gray, kp, img)
# 图像显示
cv.imshow('harris', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()

