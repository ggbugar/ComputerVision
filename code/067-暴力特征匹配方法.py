# 暴力特征匹配方法
# Brute_Force
# 原理：
# 使用第一组中的每个特征的描述子
#
#
#
#
#


import cv2 as cv
import numpy as np

img = cv.imread('../resources/images/shudu.png')
# 灰度化
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 创建ORB对象
orb = cv.xfeatures2d.SIFT_create()
# 进行检测，kp=surf.detect(img,...)
kp, des = orb.detectAndCompute(gray, None)
# for i in des:
#     print(i)
# 绘制关键点cv.drawKeypoint(grey,kp,img)
cv.drawKeypoints(gray, kp, img)
# 图像显示
cv.imshow('harris', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()







