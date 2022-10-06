# 暴力特征匹配方法
# Brute_Force
# 原理：
# 使用第一组中的每个特征的描述子
# 与第二组中的所有特征描述子进行匹配
# 计算他们之间的差距，然后将最接近的一个匹配返回
# 步骤：
# 1 创建匹配器 matcher=cv.BFMatcher(normalType,crossCheck)
# normalType NORM_L1用于sift,NORM_L2(default)用于surf,NORM_HAMMING、NORM_HAMMING2用于orb
# crossCheck 是否进行交叉匹配 True,False(default)
# 2 进行特征匹配 match = matcher.match(des1, des2)
# des1 sift,surf,orb等计算出的描述子
# 3 绘制匹配点 result = cv.drawMatches(img1, kp1, img2, kp2, match, None)
# img1,kp1 搜索的图和特征点
# img2,kp2 匹配的图和特征点


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
# sift = cv.xfeatures2d.SIFT_create()
# surf = cv.xfeatures2d.SURT_create()
orb = cv.ORB_create()
# 计算特征点和描述子 kp, des = orb.detectAndCompute(gray, None)
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)
# 创建匹配器 matcher = BFMatcher(normalType,crossCheck)
# NORM_L1,NORM_L2(default),NORM_HAMMING,NORM_HAMMING2
matcher = cv.BFMatcher(cv.NORM_HAMMING, False)
# 进行特征匹配
match = matcher.match(des1, des2)
# 绘制匹配点
result = cv.drawMatches(img1, kp1, img2, kp2, match, None)
# 图像显示
cv.imshow('result', result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()







