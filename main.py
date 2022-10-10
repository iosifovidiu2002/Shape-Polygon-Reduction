import turtle
import numpy as np
from sympy import Point
from turtle import Turtle, Screen
from matplotlib import pyplot as plt
from utils import read_perimeter_from_file, rearrange_points
from douglas_peucker import douglas_peucker

screen = Screen()
screen.bgpic("field.gif")

t = Turtle()

t.pencolor("red")
t.width(4)

t.speed(-1)
points = list()

def dragging(x, y):
    point = Point(x, y)
    points.append(point)
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x, y)
    t.ondrag(dragging)

def draw_points(pinpoints, color="red"):
    if not pinpoints:
        raise Exception("Empty point set!")
    for i in range(len(pinpoints)-1):
        draw_line(pinpoints[i], pinpoints[i+1], color=color)
    draw_line(pinpoints[0], pinpoints[-1])

def click_right(curr_x, curr_y):
    global points
    # points = read_perimeter_from_file("points.in")
    epsilon = 15
    # draw_points(points, color="red")
    print(f"Detected {len(points)} points")
    # points = rearrange_points(points)
    points = douglas_peucker(points, epsilon)
    print(f"Polygon {len(points)} points found")
    t.clear()
    draw_points(points, color="blue")

def move_pen(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_line(point1, point2, color="red"):
    t.pencolor(color)
    t.penup()
    t.goto(point1.x, point1.y)
    t.pendown()
    t.goto(point2.x, point2.y)
    t.penup()

def main():
    turtle.listen()

    t.ondrag(dragging)

    turtle.onscreenclick(click_right, 3)
    turtle.onscreenclick(move_pen, 2)
    screen.mainloop()


main()