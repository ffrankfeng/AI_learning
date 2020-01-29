import cv2
'''
调用opencv模块
安装opencv在cmd模式下输入 pip install opencv-python
cv2的具体配置自行搜索
'''

imagePath = '../resources/faces/1.jpg'  # 把图片赋给imagePath

# 获取人脸识别训练数据的xml文件
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# 加载分类器文档绝对地址
faceCascade.load('F:\opencv\opencv3.3\opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')


image = cv2.imread(imagePath)  # 读取刚刚放入图片值的变量
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转化为灰度图像，目的是提高计算速度
# 整个代码的核心，用来检测人脸的函数
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5,5),
    # flags = 0
)
# gray：灰度图像
# scaleFactor：官网文档说是每次图片缩小的比例,其实可以这么理解,距离相机不同的距离,物体大小是不一样的,在物体大小不一致的情况下识别一个东西是不方便的,这就需要进行多次的缩放,这就是这个参数的作用.
# minNeighbors：可以理解为每次检测时,对检测点(Scale)周边多少有效点同时检测,因为可能选取的检测点大小不足而导致遗漏
# minSize: 检测点的最小值,或者说就是检测点的最终值


print('Found {0} faces!'.format(len(faces)))  #
for (x, y, w, h) in faces:  # 通过坐标绘制矩形，x,y是左上角坐标；w,h分别是宽度和高度
	# cv2.circle(image, ((x + x + w) // 2, (y + y + h) // 2), w // 2, (255, 0, 0), 2)  #用圆形显示检测对象
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)  # 用矩形显示检测对象
    cv2.imshow("Faces found", image)  # 在窗口中显示图片
    cv2.waitKey(0)  # 每帧的显示时长，单位毫秒，0代表显示到按任意键结束
    cv2.destroyAllWindows()  # 释放窗口

