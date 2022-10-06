# ORB是FAST、BRIEF两种技术的组合
# ORB最大且唯一的优点就是可以 实时检测 检测速度大大提升
# ORB缺点 抛弃了大量数据，计算准确率没那么高
# ORB 算法开源，在cv中
#
# FAST 可以做到特征点实时检测
# BRIEF 是对已检测的特征点进行描述
#       加快了特征描述符建立的速度
#       极大降低了特征匹配时间

# SURF使用步骤 相对sift改个名字即可
#   创建ORB对象 orb = cv.ORB_create()
#   进行检测，kp=orb.detect(img,...)
#   绘制关键点cv.drawKeypoints(grey,kp,img)

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







