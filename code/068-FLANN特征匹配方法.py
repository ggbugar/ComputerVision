# flann 速度块
# flann 使用的是临近近似值，所以精度差

# 步骤：
# 1 创建匹配器
#
# 2 进行特征匹配
#
# 3 绘制匹配点
#

# 实战
import cv2 as cv
import numpy as np
# 读取图像
# 用小图到大图中去搜索
img1 = cv.imread('../resources/images/subshudu.png')
img2 = cv.imread('../resources/images/shudu.png')
# 灰度化
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
# 创建特征检测器
sift = cv.xfeatures2d.SIFT_create()
# surf = cv.xfeatures2d.SURT_create()
# orb = cv.ORB_create()
# 计算特征点和描述子 kp, des = orb.detectAndCompute(gray, None)
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)
# 创建匹配器
index_params = dict(algorithm=1, tree=5)
search_params = dict(checks=50)
matcher = cv.FlannBasedMatcher(index_params, search_params)
# 进行特征匹配,对描述子进行匹配计算
match = matcher.knnMatch(des1, des2, k=2)
# 过滤匹配点
goodMatch = []
for i, (m, n) in enumerate(match):
    if m.distance < 0.7 * n.distance:
        goodMatch.append(m)
# 绘制匹配点
result = cv.drawMatchesKnn(img1, kp1, img2, kp2, [goodMatch], None)
# 图像显示
cv.imshow('result', result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()

