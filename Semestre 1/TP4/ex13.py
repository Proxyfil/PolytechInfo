from turtle import *
speed(1000)

def motif(r):
    left(180)
    fillcolor("blue")
    for i in range(5):
        begin_fill()
        circle(r)
        end_fill()
        circle(r,150)
        right(180)
        r = r*1.5
    r = r/3
    for i in range(4):
        begin_fill()
        circle(r)
        end_fill()
        circle(r,-150)
        left(180)
        r = r/1.5

def repetition():
    position = [[0,-50],[0,50]]
    for i in range(len(position)):
        penup()
        goto(position[i])
        pendown()
        motif(5)
        left(60)

repetition()
input()