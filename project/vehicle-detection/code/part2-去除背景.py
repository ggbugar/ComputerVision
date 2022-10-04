# 去背景
# API
# createBackGroundSubtractorMOG(...) 参数大多使用默认值即可
# history = 200 毫秒值，预存多长时间的视频帧数，200，对应5帧，
# history越大越准确，但效率慢

import cv2 as cv
import numpy as np

# 创建背景
background = cv.bgsegm.createBackgroundSubtractorMOG()

# 打开视频或直接录制图像
cap = cv.VideoCapture('../resources/VD2.mp4')

while cap.isOpened():
    # 获取一帧
    ret, frame = cap.read()
    # 判断是否获取到帧并进行图像处理
    if ret:
        # 转灰度图
        grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # 降噪（高斯）
        blur = cv.GaussianBlur(grey, (7, 7), 10)
        # 降噪（中值）
        blur = cv.medianBlur(blur, 7)
        # 去除背景
        anti_background = background.apply(blur)
        # 显示图像
        cv.imshow('VD', anti_background)
    # 按q退出
    key = cv.waitKey(25)
    if key & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv.destroyAllWindows()





