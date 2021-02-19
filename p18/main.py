import random
import turtle
from turtle import Screen, Turtle

import heroes

print(heroes.gen())
turtle.colormode(255)
obj = Turtle()
# turtle.shape("turtle")
# turtle.color("red")
# for i in range(3):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()
# for i in range(4):
#     turtle.forward(50)
#     turtle.right(90)
#
colors = ["red", "green", "blue", "yellow"]
#
# for sides in range(4, 10):
#     turtle.pencolor(random.choice(colors))
#     for i in range(sides):
#         angle = 360 / sides
#         turtle.forward(100)
#         turtle.right(angle)

def random_color(): return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

obj.speed("fastest")
# directions = [0, 90, 180, 270]
# obj.pensize(15)
# for sides in range(200):
#     obj.pencolor(random_color())
#     obj.forward(20)
#     obj.setheading(random.choice(directions))

def draw_spiro(gap_size):
    for i in range(int(360 / gap_size)):
        obj.color(random_color())
        obj.circle(100)
        obj.setheading(obj.heading() + gap_size)

draw_spiro(5)

screen = Screen()
screen.exitonclick()