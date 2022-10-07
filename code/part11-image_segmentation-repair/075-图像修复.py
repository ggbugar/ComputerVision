# 图像修复
# inpaint(
# img,要修复的图片
# mask,要修复的地方的黑背景图片
# inpaintRadius,每个点的圆形领域半径,修复半径
# flags,INOAINTNS,INPAINT_TELEA
# )
import cv2 as cv
import numpy as np

img = cv.imread('../../resources/images/inpaint.png')
mask = cv.imread('../../resources/images/inpaint_mask.png', 0)

dst = cv.inpaint(img, mask, 5, cv.INPAINT_TELEA)

cv.imshow('img', img)
cv.imshow('mask', mask)
cv.imshow('dst', dst)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()


