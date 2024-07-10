import turtle
t = turtle.Turtle()
t.color("red")
t.speed(0)
t.width(10)

def square(side_length):
    for side in range(4):
        t.forward(side_length)
        t.right(90)

def spiral(sides):
    t = turtle.Turtle()
    t.speed(0)
    t.width(6)
    t.color("cyan")
    y = turtle.Turtle()
    y.speed(0)
    y.width(6)
    y.color("cyan")
    for n in range(sides):
        t.forward(n)
        t.right(20)
        y.forward(n)
        y.left(20)

spiral(100)
  
def spin(sides, turn, color, width):
    t = turtle.Turtle()
    t.color(color)
    t.width(width)
    for n in range(sides):
        t.forward(n)
        t.right(turn)

spin(100,40,"yellow",5)
for side in range(20):
    t.forward(side*30)
    
    t.right(120)

