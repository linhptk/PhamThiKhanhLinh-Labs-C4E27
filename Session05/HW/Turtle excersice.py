# 1
# def say_helloworld():
#     for i in range(3):
#         print("Hello World")
# say_helloworld()

# 2
# def add_two_number(a,b):
#     print(a+b)
# add_two_number(5,5)

# 3
# from turtle import *
# shape("turtle")
# def draw_shapes(length,line_color):
#     color(line_color)
#     for i in range(4):
#         forward(length)
#         left(90)
# draw_shapes(100,"blue")

# 4
from turtle import *
shape("turtle")
def draw_square(length,line_color):
    color(line_color)
    for i in range(4):
        forward(length)
        left(90)
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

# 5
from turtle import *
shape("turtle")
def draw_star(x,y,length):
    for i in range(5):
        x = left(x)
        y = right(y)
        forward(100)

