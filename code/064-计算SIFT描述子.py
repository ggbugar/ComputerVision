# 计算SIFT描述子
# 关键点：位置，大小和方向
# 关键点描述子：记录了关键点周围对其有贡献的像素点的一组向量值
#            其不受仿射变换，光照变换等影响
# 计算SIFT描述子
# kp, des = sift.compute(img, kp)
# 描述子作用就是用于特征匹配
# 同时计算关键点和描述子 最常用！！！
# kp,des = sift.detectAndCompute(img, mask)
# mask指明对那个区域进行计算 None指定所有区域
# 返回值是一个矩阵，每一行都是一个描述子

import cv2 as cv
import numpy as np

img = cv.imread('../resources/images/shudu.png')
# 灰度化
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 创建SIFT对象
sift = cv.xfeatures2d.SIFT_create()
# 进行检测，kp=sift.detect(img,...)
kp, des = sift.detectAndCompute(gray, None)
for i in des:
    print(i)
# 绘制关键点cv.drawKeypoint(grey,kp,img)
cv.drawKeypoints(gray, kp, img)
# 图像显示
cv.imshow('harris', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()

