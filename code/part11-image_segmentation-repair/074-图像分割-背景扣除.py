# 图像及视频背景扣除
# 视频是一组连续的帧
# 帧与帧之间关系密切GOP
# 在GOP中，背景是基本不变的
# API
# createBackgroundSubtractorMOG

# 实战 提取视频cv.mp4，去背景后保存为anti-background-cv.mp4
import cv2 as cv
import numpy as np

# 创建窗口
cv.namedWindow("cv.mp4")
cv.namedWindow("anti-background-cv.mp4")
# 获取视频设备
cap = cv.VideoCapture('../../resources/videos/cv.mp4')
# 获取背景对象
mog = cv.bgsegm.createBackgroundSubtractorMOG()
# mog = cv.createBackgroundSubtractorMOG2()
# 可以计算出阴影部分，但会产生很多噪点
# mog = cv.bgsegm.createBackgroundSubtractorGMG()
# 可以计算出阴影部分，解决了噪点问题
# 但是，开始会等一小会儿时间黑屏，初始化帧数为120，可以调整初始化帧的数量
# 设置编码格式fourcc
fourcc = cv.VideoWriter_fourcc(*'mp4v')
# 创建VideoWriter
videoWriter = cv.VideoWriter('../../resources/videos/anti-background-cv.mp4', fourcc, 30, (1080, 720), True)
# 读取并保存帧
while cap.isOpened():
    # 从视频读取帧
    ret, frame = cap.read()
    if ret:
        # 去背景
        anti_background_frame = mog.apply(frame)
        # 写数据（帧）到多媒体文件
        anti_background_frame = cv.resize(anti_background_frame, (1080, 720))
        videoWriter.write(anti_background_frame)
        # 设置窗口大小
        cv.resizeWindow('cv.mp4', 1080, 720)
        cv.resizeWindow('anti-background-cv.mp4', 1080, 720)
        # 显示原来的视频
        cv.imshow('cv.mp4', frame)
        # 将去背景的视频在窗口中显示
        cv.imshow('anti-background-cv.mp4', anti_background_frame)
        # 设置每张图片显示的时间，可以以此设置播放帧率
        key = cv.waitKey(30)
        if key & 0xFF == ord('q'):
            break
    else:
        break
# 释放VideoCapture
cap.release()
# 释放VideoWriter
videoWriter.release()
# 关闭窗口
cv.destroyAllWindows()


