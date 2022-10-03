# Mat的浅拷贝与深拷贝
# Mat的浅拷贝
# Mat A
# A=cv.imread(file, IMREAD_COLOR)
# Mat B(A)
# Mat的深拷贝
# C++ API
# cv::Mat::clone()
# cv::Mat::copyTo()
# python API
# copy()
# Mat的深拷贝

# 实例
# 读取图像
import cv2 as cv

img = cv.imread('../resources/images/image.png')
# 浅拷贝
img2 = img
# 深拷贝
img3 = img.copy()
# 显示图像
img[10:100, 10:100] = [0, 0, 255]
cv.imshow('img', img)
cv.imshow('img2', img2)
cv.imshow('img3', img3)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')
    cv.destroyWindow('img2')
    cv.destroyWindow('img3')















