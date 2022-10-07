# 实战 色彩空间转换
# 颜色空间转换API
# cvt_img = cv.cvtColor(img, cv.COLOR_...)
import cv2 as cv


def callback():
    pass


#
cv.namedWindow('color', cv.WINDOW_NORMAL)
#
img = cv.imread('../../resources/images/image.png')

colorSpaces = [cv.COLOR_BGR2RGBA,
               cv.COLOR_BGR2BGRA,
               cv.COLOR_BGR2GRAY,
               cv.COLOR_BGR2HSV_FULL,
               cv.COLOR_BGR2YUV]

cv.createTrackbar('curColor', 'color', 0, len(colorSpaces), callback)

while True:
    index = cv.getTrackbarPos('curColor', 'color')
    # 颜色空间转换API
    cvt_img = cv.cvtColor(img, colorSpaces[index])
    #
    cv.imshow('color', cvt_img)
    key = cv.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv.destroyWindow('color')
