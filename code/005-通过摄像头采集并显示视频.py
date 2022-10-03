# Video acquisition API
# VideoCapture()
#     参数为0时候使用摄像头获取视频帧
#     参数为媒体文件名或者媒体文件路径时候通过媒体文件获取视频帧
# cap.read()
#     返回两个值
#     ret为状态值，读到帧为true
#     frame为视频帧
# cap.release()
#     释放VideoCapture

# 通过摄像头获取视频
import cv2 as cv
# 创建窗口
cv.namedWindow('video', cv.WINDOW_AUTOSIZE)
cv.resizeWindow('video', 480, 270)
# 获取视频设备
cap = cv.VideoCapture(0)
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
