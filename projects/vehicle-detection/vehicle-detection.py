import cv2 as cv
import numpy as np
import math


# 车辆中心点坐标计算
def center(x, y, width, height):
    return int(x + width / 2), int(y + height / 2)


# 车辆重复检测
def not_repeated(img, template):
    # 灰度化
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
    # 取模板的长宽
    height, width = template.shape[:2]
    # 模板匹配
    result = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
    # 获取匹配度相关系数，越小越相关min_val
    (min_val, max_val, min_loc, max_loc) = cv.minMaxLoc(result)
    # 取匹配的图的左上角坐标
    (start_x, start_y) = max_loc
    # 取中心点
    center_x, center_y = center(start_x, start_y, width, height)
    # 判断该车是否重复
    if min_val < 0.5 and (line_height - offset < center_y) and (center_y < line_height + offset):
        return False
    return True


# 传入图像高度（像素点），摄像机俯视角度值，摄像机摄像范围角度
def get_line_height(video_height, angle_look, angle_wide):
    # 角度值转弧度值
    angle_look = angle_look * math.pi / 180
    angle_wide = angle_wide * math.pi / 180
    # 获取line_height
    line_h = video_height * (math.tan(angle_look + angle_wide)-math.tan(angle_look)) / (
            math.tan(angle_look + angle_wide) - math.tan(angle_look - angle_wide))
    return int(line_h)


# 传入图像高度（像素点），摄像机俯视角度值，摄像机摄像范围角度，检测带偏移角度
def get_offset(video_height, angle_look, angle_wide, angle_offset):
    # 角度值转弧度值
    angle_look = angle_look * math.pi / 180
    angle_wide = angle_wide * math.pi / 180
    angle_offset = angle_offset * math.pi / 180
    # 获取offset
    off = video_height * (math.tan(angle_look+angle_offset) - math.tan(angle_look)) / (
            math.tan(angle_look + angle_wide) - math.tan(angle_look - angle_wide))
    return int(off)


# 创建背景
background = cv.bgsegm.createBackgroundSubtractorMOG(history=1000)

# 设置并获取形态学卷积内核Kernel
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))

# 设置车辆大小限制
min_area = 900
min_w = 30
min_h = 30

# 车数量统计
count = 0

# 画线的高度
line_height = get_line_height(720, 50, 15)

# 线的偏移量,形成偏移带
# offset有默认值13
offset = 13
# offset = get_offset(video_height, angle_look, angle_wide, angle_offset):

# 创建窗口
cv.namedWindow('VD')
# 设置窗口尺寸
cv.resizeWindow('VD', 1080, 720)
# 打开视频或直接录制图像
cap = cv.VideoCapture('../dataSet/videos/MVI_12.mp4')
# 获取第一帧图像用与第一次模板匹配
ret, pre_frame = cap.read()
# 循环处理视频图像
while cap.isOpened():
    # 读取帧
    ret, frame = cap.read()
    if ret:
        # 转灰度图
        grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # 由于一些树叶也会动，形成噪点，所以进行去噪
        # 降噪（高斯）
        blur = cv.GaussianBlur(frame, (9, 9), 5)
        # 降噪（中值）去除背景中的胡椒点
        blur = cv.medianBlur(blur, 5)
        # 去除背景
        anti_background = background.apply(blur)
        # 腐蚀去除小噪点
        erode = cv.erode(anti_background, kernel, iterations=3)
        # 膨胀补齐残缺
        dilate = cv.dilate(erode, kernel, iterations=2)
        # 闭操作，去掉物体车辆内部的小斑块
        closed = cv.morphologyEx(dilate, cv.MORPH_CLOSE, kernel)
        closed = cv.morphologyEx(closed, cv.MORPH_CLOSE, kernel)
        # 查找轮廓 findContours返回轮廓和层级关系
        # 只要外轮廓cv.RETR_EXTERNAL
        contours, hierarchy = cv.findContours(closed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        # 边缘检测完后画检测线（区域）
        cv.line(frame, (0, line_height), (frame.shape[1], line_height), (255, 0, 0), 2)
        # 创建一张空图
        empty = np.zeros(frame.shape, np.uint8)
        # 车辆统计模块
        # 遍历轮廓
        for (index, contour) in enumerate(contours):
            # 在空图上画轮廓
            cv.drawContours(empty, contour, -1, (0, 0, 255), 1)
            # 获取车辆的最大外接矩阵
            (x, y, w, h) = cv.boundingRect(contour)
            # 对轮廓的外接矩形的宽高进行判断
            # 以验证该轮廓是否是有效的车辆
            # 有效车辆判断条件:
            isValid = cv.contourArea(contour) > min_area and (w >= min_w) and (h >= min_h)
            # 如果是有效车辆则尝试统计
            if isValid:
                # 对于有效的车绘制外接矩阵
                cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # 在空图上画外接矩形
                cv.rectangle(empty, (x, y), (x + w, y + h), (0, 0, 255), 2)
                # 获取车辆中心点
                (px, py) = center(x, y, w, h)
                # 对进入区域内的车辆进行计数统计
                if (line_height - offset < py) and (py < line_height + offset):
                    # 取车辆子图做模板
                    template = frame[y:y + h, x:x + w]
                    # 判断是否重复
                    if not_repeated(pre_frame, template):
                        count += 1
                        # 打印车辆数量
                        print(count)
            # 如果不是有效车辆则查看下一个轮廓
            else:
                continue
        # 显示车辆数量统计结果
        cv.putText(frame, 'number of vehicles:' + str(count), (0, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # 更新pre_frame
        pre_frame = frame
        # 显示图像
        cv.imshow('VD', frame)
        # cv.imshow('anti_background', anti_background)
        # cv.imshow('closed', closed)


    # 按q退出
    key = cv.waitKey(40)
    if key & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
# 清除窗口
cv.destroyAllWindows()
