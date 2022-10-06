# SIFT速度慢，因此有了SURF
# SURF 使用步骤 相对sift改个名字即可
#   创建SURF对象 sift = cv.xfeatures2d.SURF_create()
#   进行检测，kp=surf.detect(img,...)
#   绘制关键点cv.drawKeypoints(grey,kp,img)

import cv2 as cv
import numpy as np

img = cv.imread('../resources/images/shudu.png')
# 灰度化
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 创建SURF对象
surf = cv.xfeatures2d.SIFT_create()
# 进行检测，kp=surf.detect(img,...)
kp, des = surf.detectAndCompute(gray, None)
# for i in des:
#     print(i)
# 绘制关键点cv.drawKeypoint(grey,kp,img)
cv.drawKeypoints(gray, kp, img)
# 图像显示
cv.imshow('harris', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()



