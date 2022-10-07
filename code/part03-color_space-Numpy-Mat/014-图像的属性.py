# 访问Mat的属性
# 访问image的属性
import cv2 as cv
# 读取图像
img = cv.imread('../../resources/images/image.png')
# shape 高 宽 通道数 常用！！！
print(img.shape)
# 占用空间大小
# width * height * channel
print(img.size)
# 图像中每个元素的位深
print(img.dtype)