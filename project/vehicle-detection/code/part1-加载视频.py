import cv2 as cv
import numpy as np

# 打开视频或直接录制图像
cap = cv.VideoCapture('../resources/VD2.mp4')

while cap.isOpened():
    # 获取一帧
    ret, frame = cap.read()
    if ret:
        cv.imshow('VD', frame)
    # 按q退出
    key = cv.waitKey(25)
    if key & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv.destroyAllWindows()





