# 图像查找
# 特征匹配+单应性矩阵

# 单应性矩阵


# 图像查找
import cv2 as cv
import numpy as np
# 读取图像
# 用小图到大图中去搜索
img1 = cv.imread('../../resources/images/subshudu.png')
img2 = cv.imread('../../resources/images/shudu.png')
# 灰度化
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
# # 创建特征转换对象
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
if len(goodMatch) >= 4:
    # 通过匹配点查找单应性矩阵H
    srcPts = np.float32([kp1[m.queryIdx].pt for m in goodMatch]).reshape(-1, 1, 2)
    dstPts = np.float32([kp2[m.trainIdx].pt for m in goodMatch]).reshape(-1, 1, 2)
    H, _ = cv.findHomography(srcPts, dstPts, cv.RANSAC, 5.0)
    # 透视变换
    # 获取图的长宽
    height, width, channel = img1.shape
    # pts 要搜索的图的四个角点
    pts = np.float32([[0, 0], [0, height-1], [width-1, height-1], [width-1, 0]]).reshape(-1, 1, 2)
    # 透视变换
    dst = cv.perspectiveTransform(pts, H)
    # 在大图中框出小图
    result = cv.polylines(img2, [np.int32(dst)], True, (0, 0, 255))
else:
    print('the number of goog match is less than 4')
    exit()

# 绘制匹配点
# result = cv.drawMatchesKnn(img1, kp1, img2, kp2, [goodMatch], None)

# 图像显示
cv.imshow('img1',img1)
cv.imshow('result', result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()






