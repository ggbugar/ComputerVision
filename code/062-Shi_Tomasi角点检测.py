# 改进版本
# goodFeaturesToTrack(img,maxCorners,...)
# img
# maxCorners 检测的最大角点数 0表示无限制
# qualityLevel 角点的质量 小于1的正数，一般0.01到0.1之间
# minDistance 角之间的最小欧式距离，忽略小于此距离的角点
# mask 感兴趣的区域
# blockSize 检测窗口
# useHarrisDetector 是否使用Harris算法默认False
# k 默认0.04
# 返回值为角点的坐标,32位浮点型，需要转整型
# 更常用！！！

import cv2 as cv
import numpy as np

maxCorners = 1000
qualityLevel = 0.01
minDistance = 10
img = cv.imread('../resources/images/shudu.png')
# 灰度化
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
corners = cv.goodFeaturesToTrack(gray, maxCorners, qualityLevel, minDistance)
# 转整型
corners = np.int0(corners)
# 角点展示
for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, (255, 0, 0), -1)
# 图像显示
cv.imshow('harris', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
