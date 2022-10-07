import cv2 as cv
import numpy as np

# 创建背景
background = cv.bgsegm.createBackgroundSubtractorMOG(history=500)
# 设置并获取形态学卷积内核Kernel
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
# 创建窗口
cv.namedWindow('VD')
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
        # 创建一张空图
        empty = np.zeros(frame.shape, np.uint8)
        # 遍历轮廓
        for(index, contour) in enumerate(contours):
            # 在空图上画轮廓
            cv.drawContours(empty, contour, -1, (0, 0, 255), 1)
            # 获取车辆的最大外接矩阵
            (x, y, w, h) = cv.boundingRect(contour)
            # 在空图上画外接矩形
            cv.rectangle(empty, (x, y), (x+w, y+h), (0, 0, 255), 2)
            # 在原图上画最大外接矩阵
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        # 显示轮廓方框图和画框原图
        # cv.imshow('grey', grey)
        # cv.imshow('blur', blur)
        # cv.imshow('anti_background', anti_background)
        # cv.imshow('erode', erode)
        # cv.imshow('dilate', dilate)
        # cv.imshow('opened', opened)
        # cv.imshow('closed', closed)
        cv.imshow('outline', empty)
        # 重新设置窗口尺寸
        cv.resizeWindow('VD', 1080, 720)
        # 显示图像
        cv.imshow('VD', frame)

    # 按q退出
    key = cv.waitKey(25)
    if key & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

