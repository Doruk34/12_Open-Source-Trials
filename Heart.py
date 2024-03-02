import turtle

pen = turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def text1():
    pen.up()
    pen.setpos(-5, 95)
    pen.down()
    pen.color('yellow')
    pen.write("I Love You", align="center", font=("Courier", 14, "normal"))
    

heart()
text1()
pen.hideturtle()
turtle.done()
pen.hideturtle()
turtle.done()

