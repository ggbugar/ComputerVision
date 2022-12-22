# 将大量命好名的图片合成一个视频
# 说明：
# 需要修改的几个参数：
# 最大图片数 max_index
# 图片路径前缀 prefix
# 写入文件路径 videoPath

import cv2 as cv

# 需要修改的几个参数：
# 最大图片数
max_index = 1000
# 图片路径前缀
prefix = '../dataSet/images/MVI_16/'
# 写入文件路径
videoPath = '../dataSet/videos/MVI_16.mp4'
# 图片后缀名
suffix = '.jpg'


# 获取读取图片的路径
def get_path(index):
    global suffix, prefix
    if index < 10:
        return prefix + 'img0000' + str(i) + suffix
    elif index < 100:
        return prefix + 'img000' + str(i) + suffix
    elif index < 1000:
        return prefix + 'img00' + str(i) + suffix
    elif index < 10000:
        return prefix + 'img0' + str(i) + suffix
    else:
        exit()


# 设置编码格式fourcc
fourcc = cv.VideoWriter_fourcc(*'mp4v')
# 写入文件的帧数
frames = 25
# 分辨率
width, height = 960, 540

# 创建VideoWriter
videoWriter = cv.VideoWriter(videoPath, fourcc, frames, (width, height), True)

# 图片计数
i = 0
# 读取并保存帧
while i < max_index:
    i += 1
    path = get_path(i)
    frame = cv.imread(path)
    # 写数据（帧）到多媒体文件
    videoWriter.write(frame)

# 释放VideoWriter
videoWriter.release()
