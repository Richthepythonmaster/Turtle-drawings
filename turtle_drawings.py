from turtle import *

speed(5)


def drawhead():
    # Draws the head
    penup()
    goto(-60, 30)
    pendown()
    color("green")
    begin_fill()
    for i in range(2):
        forward(30)
        right(90)
        forward(30)
        right(90)
    end_fill()


def draweyes():
    # Draws the eyes
    goto(-50, 20)
    color("black")
    dot(5)


def drawshell():
    # Draws the shell
    penup()
    goto(-30, 0)
    pendown()
    color("brown")
    begin_fill()
    for i in range(2):
        forward(80)
        left(90)
        forward(60)
        left(90)
    end_fill()


def drawfrontleg():
    # Draws the front leg
    penup()
    goto(-30, 0)
    pendown()
    color("green")
    begin_fill()
    for x in range(2):
        forward(10)
        right(90)
        forward(20)
        right(90)
    end_fill()


def drawbackleg():
    # Draws the back leg
    penup()
    goto(40, 0)
    pendown()
    color("green")
    begin_fill()
    for m in range(2):
        forward(10)
        right(90)
        forward(20)
        right(90)
    end_fill()


def drawtail():
    # Draws the tail
    penup()
    goto(50, 0)
    pendown()
    color("green")
    begin_fill()
    for i in range(2):
        forward(20)
        left(90)
        forward(10)
        left(90)
    end_fill()


drawhead()
draweyes()
drawshell()
drawfrontleg()
drawbackleg()
drawtail()
