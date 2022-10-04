import cv2 as cv
import numpy as np

# 设置车辆大小
min_w = 90
min_h = 90
max_w = 500
max_h = 500
# 存放有效车辆的数组
cars = []
# 车数量统计
count = 0
# 画线的高度
line_height = 500
# 线的偏移量
offset = 10

# 设置并获取形态学卷积内核Kernel
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))


# 车辆中心点坐标计算
def center(x, y, w, h):
    return int(x + w / 2), int(y + h / 2)


# 打开视频或直接录制图像
cap = cv.VideoCapture('../resources/VD.mp4')
# 创建背景
background = cv.bgsegm.createBackgroundSubtractorMOG()
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # 转灰度图
        grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # 二值化
        maxValue = 128
        binary = cv.adaptiveThreshold(grey, maxValue, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 99, 0)
        # 降噪（高斯）
        blur = cv.GaussianBlur(binary, (3, 3), 5)
        # 去除背景
        anti_background = background.apply(blur)
        # 腐蚀去除小斑块
        erode = cv.erode(anti_background, kernel)
        # 膨胀n次
        n = 2
        dilate = cv.dilate(erode, kernel, iterations=n)
        # 开操作，去除黑背景中的小白点
        opened = cv.morphologyEx(dilate, cv.MORPH_OPEN, kernel)
        # 闭操作，去掉物体内部的小斑块
        closed = cv.morphologyEx(opened, cv.MORPH_CLOSE, kernel)
        # 查找轮廓
        contours, hierarchy = cv.findContours(closed, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        # 遍历轮廓
        outline = np.zeros(frame.shape, np.uint8)

        # 画检测线（区域）
        cv.line(frame, (0, line_height), (frame.shape[1], line_height), (0, 0, 255), 1)
        for (i, c) in enumerate(contours):
            # 在空图上画轮廓
            cv.drawContours(outline, contours, -1, (0, 0, 255), 1)
            # 获取车辆的最大外接矩阵
            (x, y, w, h) = cv.boundingRect(c)
            # 对车辆宽高进行判断
            # 以验证是否是有效的车辆
            isValid = (w >= min_w) and (h >= min_h) and (w <= max_w) and (h <= max_h)
            if not isValid:
                continue
            # 获取车辆中心点
            centers = center(x, y, w, h)
            # 车辆统计
            cars.append(centers)
            for (x, y) in cars:
                if (y > line_height-offset) and (y < line_height+offset):
                    count += 1
                    cars.remove()
                    print(count)
            # 在原图上画最大外接矩阵
            cv.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
        #  显示车辆统计信息
        cv.putText(frame, 'car count:'+str(count), (0, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
        # 显示每一帧
        cv.imshow('VD', frame)

    key = cv.waitKey(40)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv.destroyWindow('VD')
