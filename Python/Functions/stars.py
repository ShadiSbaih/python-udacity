import turtle

def star(color, sides, length, angle, distance):
    galileo = turtle.Turtle()
    galileo.color(color)  # colorful!
    galileo.width(5)  # visible!
    galileo.speed(0)  # fast!
    galileo.penup()
    galileo.left(angle)  # away from center
    galileo.forward(distance)
    galileo.pendown()  # start drawing
    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
    galileo.hideturtle()  # just the star
    
for angle in [180, 135, 90, 45, 0,-45,-90,-135,-180]:
    star("red", 7, 50, angle, 120)
    
         
for angle in [180, 135, 90, 45, 0]:
    star("blue", 5, 30, angle, 60)