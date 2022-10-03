# 通过摄像头录制并保存视频
# 保存视频
# VideoWriter
#     参数一为输出文件路径
#     参数二为多媒体文件格式（VideoWriter_fourcc)
#       cv.VideoWriter_fourcc(*'mp4v'),视频后缀名为 .mp4
#     参数三为帧率
#     参数四为分辨率大小
#       width, height = cap.get(3), cap.get(4)
#       print(width, height)
#     参数四为是否有颜色，默认为True
# write(frame)
#     参数为要写入的帧frame
# release()

import cv2 as cv
# 创建窗口
cv.namedWindow("recording")
# 设置窗口显示尺寸
cv.resizeWindow('recording', 640, 480)
# 获取视频设备
cap = cv.VideoCapture(0)
# 设置编码格式fourcc
fourcc = cv.VideoWriter_fourcc(*'mp4v')
# 创建VideoWriter
videoWriter = cv.VideoWriter('../resources/videos/recording.mp4', fourcc, 30, (640, 480), True)
# 读取并保存帧
while cap.isOpened():
    # 从摄像头读取帧
    ret, frame = cap.read()
    if ret:
        # 写数据（帧）到多媒体文件
        videoWriter.write(frame)
        # 将视频帧在窗口中显示
        cv.imshow('recording', frame)
        # 设置窗口显示尺寸
        cv.resizeWindow('recording', 640, 480)
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
cv.destroyWindow('recording')

# 读取录制的视频
cap = cv.VideoCapture('../resources/videos/recording.mp4')
while cap.isOpened():
    # 从视频读取帧
    ret, frame = cap.read()
    # 将视频帧在窗口中显示
    cv.imshow('video', frame)
    # 设置每张图片显示的时间，可以以此设置播放帧率
    key = cv.waitKey(25)
    if key & 0xFF == ord('q'):
        break
# 释放VideoCapture
cap.release()
# 关闭窗口
cv.destroyWindow('video')










