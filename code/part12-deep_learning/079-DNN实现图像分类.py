# DNN实现图像分类

# DNN使用步骤
# 读取模型，取得深度神经网络
# 读取图片、视频
# 将图片转换成张量，送入深度神经网络
# 进行分析，并得到结果

import cv2 as cv
from cv2 import dnn
import numpy as np

# 读取模型，取得深度神经网络
config = "../../resources/model/bvlc_googlenet.prototxt"
model = "../../resources/model/bvlc_googlenet.caffemodel"
net = dnn.readNetFromCaffe(config, model)
# 读取图片,转成张量
img = cv.imread('../../resources/images/smallcat.jpeg')
blob = dnn.blobFromImage(img,
                         1.0,
                         (224, 224),
                         (104, 117, 123))

# 将图片转换成张量，送入深度神经网络，并进行预测
net.setInput(blob)
r = net.forward()
# 读取类目
classes = []
path = '../../resources/model/synset_words.txt'
with open(path, 'rt') as f:
    classes = [x[x.find(" ") + 1:] for x in f]

order = sorted(r[0], reverse=True)

z = list(range(3))
for i in range(0, 3):
    z[i] = np.where(r[0] == order[i])[0][0]
    print('第', i + 1, '项，匹配', classes[z[i]], end='')
    print('类所在行：', z[i] + 1, ' ', '可能性', order[i])
