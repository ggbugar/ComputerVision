# 图像翻转
# flip(img,flipCode)
# 图像，flipCode=0上下翻转，flipCode>0 左右，flipCode<0 上下左右

import cv2 as cv

img = cv.imread('../resources/images/dog.png')
cv.imshow('img', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')

# 上下翻转
ud = cv.flip(img, 0)
cv.imshow('ud', ud)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('ud')

# 左右翻转
lr = cv.flip(img, 1)
cv.imshow('lr', lr)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('lr')

# 上下左右翻转
udlr = cv.flip(img, -1)
cv.imshow('udlr', udlr)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('udlr')

# 实战 使用flip实现视频左右翻转
# 创建窗口
cv.namedWindow("flipVideo")
# 设置窗口显示尺寸
cv.resizeWindow('flipVideo', 1080, 720)
# 获取视频
cap = cv.VideoCapture('../resources/videos/cv.mp4')
# 设置编码格式fourcc
fourcc = cv.VideoWriter_fourcc(*'mp4v')
# 创建VideoWriter
videoWriter = cv.VideoWriter('../resources/videos/flippedCV.mp4', fourcc, 30, (1080, 720), True)
# 读取并保存帧
while cap.isOpened():
    # 从摄像头读取帧
    ret, frame = cap.read()
    if ret:
        # 调整分辨率
        zoom = cv.resize(frame, (1080, 720), interpolation=cv.INTER_AREA)
        # 左右翻转
        dst = cv.flip(zoom, 1)
        # 写数据（帧）到多媒体文件
        videoWriter.write(dst)
        # 设置窗口显示尺寸
        cv.resizeWindow('flipVideo', 1080, 720)
        # 将视频帧在窗口中显示
        cv.imshow('flipVideo', dst)
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
cv.destroyWindow('flipVideo')











