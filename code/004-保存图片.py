import cv2 as cv
# 处理图片

# 创建窗口
# namedWindow('windowName')
cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
# 修改窗口尺寸
# resizeWindow('windowName'，width,height)
cv.resizeWindow('image', 640, 480)
# 读取图片
# imread(img)
img = cv.imread('../resources/images/image.png')
# 窗口绑定并展示图片
# imshow('windowName',img)
cv.imshow('image', img)
# 设置图片展示时间
# waitKey(t) t为毫秒值，t=0则一直展示
key = cv.waitKey(0)
# 按q退出
if key & 0xFF == ord('q'):
    cv.destoryAllWindow('image')
# 按s保存图片到指定目录
# imwrite('savePath',img)
elif key & 0xFF == ord('s'):
    cv.imwrite('../resources/images/savedImage.png', img)
