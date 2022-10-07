import cv2 as cv
import numpy as np

# 创建窗口
cv.namedWindow('VD')
# 打开视频或直接录制图像
cap = cv.VideoCapture('../resources/VD.mp4')
# 循环处理视频图像
while cap.isOpened():
    # 获取一帧
    ret, frame = cap.read()
    if ret:
        # 重新设置窗口尺寸
        cv.resizeWindow('VD', 1080, 720)
        # 显示图像
        cv.imshow('VD', frame)
    # 按q退出
    key = cv.waitKey(25)
    if key & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv.destroyAllWindows()





