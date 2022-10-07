# 双边滤波
# 优点 可以保留边缘 同时对边缘内区域进行平滑处理
# 处理胡椒噪音效果极差
# 作用 美颜 磨皮平滑处理
# API
# void bilateralFilter( InputArray src,
#                       OutputArray dst,
#                       int d,
#                       double sigmaColor,
#                       double sigmaSpace,
#                       int borderType = BORDER_DEFAULT );
# InputArray类型的src，输入图像，即源图像，需要为8位或者浮点型单通道、三通道的图像。
# OutputArray类型的dst，即目标图像，需要和源图片有一样的尺寸和类型。
# int类型的d，表示在过滤过程中每个像素邻域的直径。如果这个值我们设其为非正数，那么OpenCV会从第五个参数sigmaSpace来计算出它来。
# double类型的sigmaColor，颜色空间滤波器的sigma值。这个参数的值越大，就表明该像素邻域内有更宽广的颜色会被混合到一起，产生较大的半相等颜色区域。
# double类型的sigmaSpace坐标空间中滤波器的sigma值，坐标空间的标注方差。他的数值越大，意味着越远的像素会相互影响，从而使更大的区域足够相似的颜色获取相同的颜色。当d>0，d指定了邻域大小且与sigmaSpace无关。否则，d正比于sigmaSpace。
# int类型的borderType，用于推断图像外部像素的某种边界模式。注意它有默认值BORDER_DEFAULT。

# 主要管前四个参数

import cv2 as cv
import numpy as np
# 导入图片
img = cv.imread('../../resources/images/dog.png')
# 双边滤波
dst = cv.bilateralFilter(img, 7, 20, 50)
# 展示卷积前后的图片
cv.imshow('img', img)
cv.imshow('dst', dst)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyWindow('dst')



