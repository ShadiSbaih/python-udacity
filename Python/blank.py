import time
import turtle
amy = turtle.Turtle()

amy.width(5)
amy.speed(0)
amy.penup()
amy.back(340)
amy.pendown()
amy.hideturtle()
for prettycolor in ["red", "yellow", "red", "yellow", "red", "yellow", "red", "yellow","red", "yellow", "red", "yellow", "red", "yellow", "red", "yellow"]:
    amy.width(10)
    amy.color(prettycolor)
    amy.forward(200)
    amy.penup()
    amy.back(200)
    amy.right(90)
    amy.forward(10)
    amy.right(-90)
    amy.pendown()

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

# Write whatever code you want here!
stars = turtle.Turtle()
stars.width(5)
stars.speed(0)
for color in rainbow:
    stars.color(color)
    for side in [1, 2, 3, 4, 5]:
        stars.forward(50)
        stars.right(144)
    stars.right(60)
    stars.penup()
    stars.forward(50)
    stars.pendown()



time.sleep(3.0)
