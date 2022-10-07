import cv2 as cv
import numpy as np

# 第一步，创建Haar级联器
face = cv.CascadeClassifier('../resources/haarcascades/haarcascade_frontalface_default.xml')
eye = cv.CascadeClassifier('../resources//haarcascades/haarcascade_eye.xml')
mouth = cv.CascadeClassifier('../resources//haarcascades/haarcascade_mcs_mouth.xml')
nose = cv.CascadeClassifier('../resources//haarcascades/haarcascade_mcs_nose.xml')

# 第二步，导入人脸识别的图片并将其灰度化
img = cv.imread('../resources/images/p2.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 第三步，进行人脸识别
faces = face.detectMultiScale(gray, 1.1, 3)
i = 0
j = 0
# 检测出的人脸上再检测眼睛
# 遍历每张脸
for (x, y, w, h) in faces:
    # 在原图上把脸用红色框出来
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # 取每一张脸的子图
    roi_face = img[y:y + h, x:x + w]
    # 取该子图上的眼睛
    eyes = eye.detectMultiScale(roi_face, 1.1, 3)
    # 遍历每只眼睛
    for (x, y, w, h) in eyes:
        # 把眼睛在脸子图上用蓝色框出来
        cv.rectangle(roi_face, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 取脸子图的眼睛子图
        roi_eye = roi_face[y:y + h, x:x + w]
        # 给眼睛命名
        eye_name = 'eye' + str(j)
        # 眼睛数量加1
        j = j + 1
        # 显示每只眼睛
        cv.imshow(eye_name, roi_eye)
    # 脸数量加1
    i = i + 1
    # 给脸命名
    face_name = 'face' + str(i)
    # 显示每张脸
    cv.imshow(face_name, roi_face)

# mouths = mouth.detectMultiScale(gray, 1.1, 3)
# for (x, y, w, h) in mouths:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
# noses = nose.detectMultiScale(gray, 1.1, 3)
# for (x, y, w, h) in noses:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)

# 显示结果
cv.imshow('img', img)
# 按q退出
if cv.waitKey() & 0xFF == ord('q'):
    cv.destroyAllWindows()
