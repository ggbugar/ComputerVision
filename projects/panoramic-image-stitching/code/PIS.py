# 全景图像拼接

import cv2 as cv
import numpy as np


def get_homo(img1, img2):
    # 1. 创建特征转换对象
    # 2. 通过特征转换对象获得特征点和描述子
    # 3. 创建特征匹配器
    # 4. 进行特征匹配
    # 5. 过滤特征，找出有效的特征匹配点

    # 创建特征转换对象
    sift = cv.xfeatures2d.SIFT_create()
    # 计算特征点和描述子 kp, des = orb.detectAndCompute(gray, None)
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    # 创建特征匹配器
    bf = cv.BFMatcher()
    # 进行特征匹配,对描述子进行匹配计算
    matches = bf.knnMatch(des1, des2, k=2)
    # 过滤匹配点
    verify_ratio = 0.8
    verify_matches = []
    for m1, m2 in matches:
        if m1.distance < verify_ratio * m2.distance:
            verify_matches.append(m1)
    # 设获取单应性矩阵所需最少匹配点,如果匹配点数量少于折这么多，
    min_matches = 8
    if len(verify_matches) < min_matches:
        print('error:not enough matches')
        exit()
    # 通过匹配点查找单应性矩阵H
    img1_pts = []
    img2_pts = []
    for m in verify_matches:
        img1_pts.append(kp1[m.queryIdx].pt)
        img2_pts.append(kp2[m.trainIdx].pt)
    # 格式转换
    # img1_pts 格式：[(x,y),(x,y),...]
    # findHomography 需要的输入格式：[[x,y],[x,y],...]
    img1_pts = np.float32(img1_pts).reshape(-1, 1, 2)
    img2_pts = np.float32(img2_pts).reshape(-1, 1, 2)
    # 获取单应性矩阵
    H, mask = cv.findHomography(img1_pts, img2_pts, cv.RANSAC, 5.0)
    # 返回单应性矩阵
    return H


def stitch_image(img1, img2, H):
    # 1. 获得每张图片的四个角点
    # 2. 对图片进行变换（单应性矩阵使图进行旋转，平移）
    # 3. 创建一张大图，将两张图拼接到一起
    # 4. 将结果输出

    # 获得原始图的高/宽
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    # 获取两图的各自四个角点
    img1_dims = np.float32([[0, 0], [0, h1], [w1, h1], [w1, 0]]).reshape(-1, 1, 2)
    img2_dims = np.float32([[0, 0], [0, h2], [w2, h2], [w2, 0]]).reshape(-1, 1, 2)
    # 对img1的四个角点进行变换
    img1_transform = cv.perspectiveTransform(img1_dims, H)
    # 查看角点坐标
    # print(img1_dims)
    # print(img2_dims)
    # print(img1_transform)
    # 合并八个角点，以取得最大最小坐标值
    result_dims = np.concatenate((img2_dims, img1_transform), axis=0)
    # print(result_dims)
    # 取得最大最小坐标值
    [x_min, y_min] = np.int32(result_dims.min(axis=0).ravel() - 0.5)
    [x_max, y_max] = np.int32(result_dims.max(axis=0).ravel() + 0.5)
    # 图一平移的距离
    transform_dist = [-x_min, -y_min]
    # [1, 0, dx]
    # [0, 1, dy]
    # [0, 0, 1 ]
    transform_array = np.array([[1, 0, transform_dist[0]],
                                [0, 1, transform_dist[1]],
                                [0, 0, 1]])
    # 图一平移并变换
    result_img = cv.warpPerspective(img1, transform_array.dot(H), (x_max - x_min, y_max - y_min))
    # 将图二放到大图中
    result_img[transform_dist[1]:transform_dist[1] + h2, transform_dist[0]:transform_dist[0] + w2] = img2
    # 返回结果
    return result_img


# 读取图片
img1 = cv.imread('../resources/map1.png')
img2 = cv.imread('../resources/map2.png')
# 检查图片是否是横屏并转换为横屏的图像
# h, w = img1.shape[0:2]
# if w <= h:
#     # 逆时针旋转90度
#     img1 = cv.rotate(img1, cv.ROTATE_90_COUNTERCLOCKWISE)
# h, w = img2.shape[0:2]
# if w <= h:
#     # 逆时针旋转90度
#     img2 = cv.rotate(img2, cv.ROTATE_90_COUNTERCLOCKWISE)

# 重置图片尺寸1080*720
img1 = cv.resize(img1, (640, 480))
img2 = cv.resize(img2, (640, 480))
# 将两张图拼到一起，显示两张图
inputs = np.hstack((img1, img2))
cv.imshow('inputs images', inputs)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('inputs images')
# 根据特征点和计算描述子，得到单应性矩阵
H = get_homo(img1, img2)
# 进行图像拼接
result_image = stitch_image(img1, img2, H)
# 显示结果
cv.imshow('result image', result_image)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('result image')
