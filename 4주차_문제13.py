import turtle
import random
from tkinter.simpledialog import *
import math

inStr = ''
swidth, sheight = 500, 500
tX, tY, txtSize = 0, 0, 20
radius = 200
angle = 0
radian = 0

turtle.title('거북이가 나선 모양의 글자쓰기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()

inStr = askstring('문자열 입력', '거북이 쓸 문자열을 입력')
length = len(inStr)
angle = 360 / len(inStr)
theta = 360*2/length
delta = swidth/2/length

for ch in inStr :
    radian = 3.14*angle/180
    tX = radius*math.cos(radian)
    tY = radius*math.sin(radian)
    r = random.random(); g = random.random(); b = random.random()

    turtle.goto(tX, tY)

    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은 고딕', txtSize, 'bold'))
    angle += theta
    radius -= delta

turtle.done()
