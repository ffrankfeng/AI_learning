import numpy
from PIL import Image

# for i in range(4):
#     img = Image.open('../resources/pic/'+str(i)+'.jpg')
#
#     # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
#     Img = img.convert('L')
#     Img.save('../resources/pic/wb_'+str(i)+'.jpg')

# from PIL import Image
# import numpy as np
# for i in range(12):
#     a = np.asarray(Image.open('../resources/pic/'+str(i)+'.jpg').convert('L')).astype('float')
#
#     depth = 10.  # (0-100)
#     grad = np.gradient(a)  # 取图像灰度的梯度值
#     grad_x, grad_y = grad  # 分别取横纵图像梯度值
#     grad_x = grad_x * depth / 100.
#     grad_y = grad_y * depth / 100.
#     A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
#     uni_x = grad_x / A
#     uni_y = grad_y / A
#     uni_z = 1. / A
#
#     vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
#     vec_az = np.pi / 4.  # 光源的方位角度，弧度值
#     dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x 轴的影响
#     dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y 轴的影响
#     dz = np.sin(vec_el)  # 光源对z 轴的影响
#
#     b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
#     b = b.clip(0, 255)
#
#     im = Image.fromarray(b.astype('uint8'))  # 重构图像
#     im.save('../resources/pic/res_'+str(i)+'.jpg')


# img = Image.open('../resources/dian_pic/test3.jpg')
# # # 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
# Img = img.convert('L')
# threshold = 220
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# # 图片二值化
# photo = Img.point(table, '1')
#
# print(table)
# photo.save("test3.jpg")
# img = Image.open("test3.jpg")
# matrix = numpy.asarray(img)
# import matplotlib.pyplot as plt
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=" ")
#     print()
img = Image.open("test3.jpg")
reIm = img.resize((1334, 1001), Image.ANTIALIAS)
im_arr = numpy.array(reIm.convert('L'))
threshold = 200  # 阙值
for i in range(1001):
    for j in range(1334):
        im_arr[i][j] = 255 - im_arr[i][j]
        if (im_arr[i][j] < threshold):
            im_arr[i][j] = 0
        else:
            im_arr[i][j] = 255
# nm_arr = im_arr.reshape([1, 784])
# nm_arr = nm_arr.astype(numpy.float32)
# img = numpy.multiply(nm_arr, 1.0 / 255.0)
# print(im_arr)
for i in range(1001):
    for j in range(1334):
        f = open("read.txt","a+")
        f.write(str(im_arr[i][j])+" ")
        f.close()
    f = open("read.txt", "a+")
    f.write("\n")
    f.close()
