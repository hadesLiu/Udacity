# -*- coding: utf-8 -*-
# author: hiro
import turtle


def draw_flower():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(30)

    total = 360 / 10
    for i in range(total):
        for i in range(3):
            brad.forward(100)
            brad.right(120)
        brad.right(10)

    brad.right(90)
    brad.forward(200)

    window.exitonclick()

draw_flower()