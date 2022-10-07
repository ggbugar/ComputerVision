# 通过Haar定位车牌的大体位置
# 对车牌图像进行预处理
# 调用tesseract进行文字识别

import cv2 as cv
# import pytesseract

# 第一步，创建Haar级联器
plate = cv.CascadeClassifier('../resources/haarcascades/haarcascade_russian_plate_number.xml')

# 第二步，导入人脸识别的图片并将其灰度化
img = cv.imread('../resources/images/chinacar.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 第三步，检测车牌的位置
plates = plate.detectMultiScale(gray, 1.1, 3)
# 将车牌框出来
for (x, y, w, h) in plates:
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# 对车牌图像进行预处理
# 提取车牌子图
roi = gray[y:y+h, x:x+w]
# 二值化
ret, binary = cv.threshold(roi, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
# 形态学处理
# 滤波去除噪点
# 缩放

# 调用tesseract进行文字识别
# result = pytesseract.image_to_string(binary, lang='chi_sim+eng', config='--psm 8 --oem 3')

cv.imshow('plate', img)
# print(result)
cv.waitKey(0)

