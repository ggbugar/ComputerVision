# 图像旋转
# totate(img,totateCode)
# totateCode= ROTATE_90_CLOCKWISE 顺时针旋转90度
# totateCode= ROTATE_90_COUNTERCLOCKWISE 逆时针旋转90度
# totateCode= ROTATE_180 旋转180度

import cv2 as cv

img = cv.imread('../../resources/images/dog.png')
cv.imshow('img', img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('img')

# 顺时针旋转90度
result = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
cv.imshow('result', result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('result')

# 逆时针旋转90度
result = cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)
cv.imshow('result', result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('result')

# 旋转180度
result = cv.rotate(img, cv.ROTATE_180)
cv.imshow('result', result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('result')












