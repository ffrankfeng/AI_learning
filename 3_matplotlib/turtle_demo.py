# -*- coding:utf-8 -*-
import turtle as t

from PIL import Image
import numpy
import time

def draw_h():
    img = Image.open("test2.jpg")
    reIm = img.resize((400, 400), Image.ANTIALIAS)
    im_arr = numpy.array(reIm.convert('L'))
    threshold = 200  # 阙值
    t.screensize(400, 400, "pink")
    t.screensize()  # 画布默认大小（400，300）像素
    t.pensize(1)
    t.Turtle().screen.delay(0)
    t.pu()
    t.speed(0)
    t.begin_fill()
    for i in range(400):
        for j in range(400):
            im_arr[i][j] = 255 - im_arr[i][j]
            if (im_arr[i][j] < threshold):
                im_arr[i][j] = 0
            else:
                im_arr[i][j] = 255
            if im_arr[i][j] ==255:

                t.goto(200-j,200-i)
                t.pd()
                t.circle(0.5)
                t.pu()

    t.end_fill()

def draw_square():
    img = Image.open("test3.jpg")
    reIm = img.resize((600, 450), Image.ANTIALIAS)
    im_arr = numpy.array(reIm.convert('L'))
    threshold = 200  # 阙值
    t.screensize(900, 700, "pink")
    t.screensize()  # 画布默认大小（400，300）像素
    t.pensize(1)
    t.Turtle().screen.delay(0)
    t.pu()
    t.speed(0)
    t.begin_fill()
    for i in range(450):
        for j in range(600):
            im_arr[i][j] = 255 - im_arr[i][j]
            if (im_arr[i][j] < threshold):
                im_arr[i][j] = 0
            else:
                im_arr[i][j] = 255
            if im_arr[i][j] ==255:

                t.goto(300-j,300-i)
                t.pd()
                t.circle(0.5)
                t.pu()

    t.end_fill()
# 曲线移动
def curveMove():
    for i in range(200):
        t.right(1)
        t.forward(1)


def drawHeart():
    t.goto(-300,-225)
    t.speed(0) # 画笔速度调到最高
    t.color('red','pink')
    t.begin_fill()
    t.left(140) # 逆时针旋转140度
    t.forward(111.65) # 向前移动111.65个像素
    curveMove() # 画曲线
    t.left(120) # 逆时针旋转120度
    curveMove() # 继续画曲线
    t.forward(111.65) # 向前移动111.65个像素
    t.end_fill()
    time.sleep(1)
draw_square()