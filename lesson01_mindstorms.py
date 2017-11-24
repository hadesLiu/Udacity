# -*- coding: utf-8 -*-
# author: hiro
import turtle

def draw():
    window = turtle.Screen()
    window.bgcolor("red")

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed("2")
    for i in range(4):
        brad.forward(100)
        brad.right(90)


def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("yellow")
    angie.circle(100)

def draw_triangle():
    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("green")
    for i in range(3):
        angie.forward(100)
        angie.right(120)

draw()