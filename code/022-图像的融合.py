# 图像的融合
# addWeighted(imageA, alpha权重,imageB, bate, gamma静态权重)
# 注意 图像大小必须一致

# 实例
import cv2 as cv
import numpy as np

background = cv.imread('../resources/images/background.png')
dog = cv.imread('../resources/images/dog.png')

result = cv.addWeighted(background, 0.3, dog, 0.7, 0)
cv.imshow('result', result)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('result')










