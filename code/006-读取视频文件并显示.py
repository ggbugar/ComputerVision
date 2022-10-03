# 通过多媒体文件获取视频帧
import cv2 as cv
# 创建窗口
cv.namedWindow('video', cv.WINDOW_AUTOSIZE)
cv.resizeWindow('video', 360, 240)
# 读取多媒体文件
cap = cv.VideoCapture('../resources/videos/cv.mp4')
while True:
    ret, frame = cap.read()
    cv.imshow('video', frame)
    # 设置每张图片显示的时间，可以以此设置播放帧率
    key = cv.waitKey(10)
    if key & 0xFF == ord('q'):
        break
# 释放VideoCapture
cap.release()
cv.destroyWindow('video')
