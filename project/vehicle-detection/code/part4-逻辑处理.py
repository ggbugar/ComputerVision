import cv2 as cv
import numpy as np

# 创建背景
background = cv.bgsegm.createBackgroundSubtractorMOG(history=500)
# 设置并获取形态学卷积内核Kernel
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))


# 车辆中心点坐标计算
def center(x, y, w, h):
    return int(x + w / 2), int(y + h / 2)


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
line_height = 360

# 线的偏移量,形成偏移带
offset = 36

# 打开视频或直接录制图像
cap = cv.VideoCapture('../resources/VD2.mp4')
# 循环处理视频图像
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # 转灰度图
        grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # 降噪（高斯）
        blur = cv.GaussianBlur(frame, (7, 7), 10)
        # 降噪（中值）去除背景中的胡椒点
        blur = cv.medianBlur(blur, 5)
        # 去除背景
        anti_background = background.apply(blur)
        # 腐蚀去除小斑块
        erode = cv.erode(anti_background, kernel)
        # 膨胀n次
        n = 2
        dilate = cv.dilate(erode, kernel, iterations=n)
        # 开操作，去除黑背景中的小白点
        opened = cv.morphologyEx(erode, cv.MORPH_OPEN, kernel)
        # 闭操作，去掉物体内部的小斑块
        closed = cv.morphologyEx(dilate, cv.MORPH_CLOSE, kernel)
        # 查找轮廓 findContours返回轮廓和层级关系
        contours, hierarchy = cv.findContours(closed, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        # 只要外轮廓
        # contours, hierarchy = cv.findContours(closed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        # 边缘检测完后画检测线（区域）
        cv.line(frame, (0, int(frame.shape[1] * 0.75)), (frame.shape[0], int(frame.shape[1] * 0.75)), (0, 0, 255), 4)
        # 创建一张空图
        empty = np.zeros(frame.shape, np.uint8)
        # 遍历轮廓
        for (index, contour) in enumerate(contours):
            # 在空图上画轮廓
            cv.drawContours(empty, contour, -1, (0, 0, 255), 1)
            # 获取该轮廓(车辆)的最大外接矩阵
            (x, y, w, h) = cv.boundingRect(contour)
            # 对轮廓的外接矩形的宽高进行判断
            # 以验证该轮廓是否是有效的车辆
            # 有效车辆判断条件:
            isValid = (w >= min_w) and (h >= min_h) and (w <= max_w) and (h <= max_h)
            # 如果不是有效车辆则查看下一个轮廓
            if isValid:
                # 获取车辆中心点
                carCenterPoint = center(x, y, w, h)
                # 将车辆中心点加入数组
                cars.append(carCenterPoint)
                for (x, y) in cars:
                    # 对进入区域内的车辆进行计数统计
                    if (y > line_height - offset) and (y < line_height + offset):
                        count += 1
                        cars.remove((x, y))
                        print(count)
                # 在空图上画外接矩形
                cv.rectangle(empty, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # 在原图上画最大外接矩阵
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            else:
                continue
        # 显示轮廓方框图和画框原图
        cv.imshow('outline', empty)
        cv.imshow('VD', frame)

    # 按q退出
    key = cv.waitKey(25)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

